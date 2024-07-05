from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .models import Task

from django.db import connection
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer, TaskSerializer, UserSerializer





class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class TokenRefreshView(views.APIView):
    def post(self, request):
        token = request.data.get("refresh", None)

        if not token:
            return Response({"error": "refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(token)
            access_token = str(refresh_token.access_token)
            return Response({"access": access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


class TaskView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, task_id):
        user_id = request.user.id
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM selteq_task WHERE user_id = %s and id = %s ORDER BY created_at DESC LIMIT 1",
                [user_id, task_id]
            )
            row = cursor.fetchone()
            if row:
                task = {
                    'id': row[0],                    
                    'title': row[1],
                    'user_id': row[2],
                    'duration': row[3],
                    'created_at': row[4].isoformat(),
                    'updated_at': datetime.utcfromtimestamp(row[5]).isoformat()
                }
                return Response(task)
            return Response({'message': 'No task found'}, status=status.HTTP_404_NOT_FOUND)
    

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            duration = serializer.validated_data['duration']
            user = request.user

            # Create a new task record in the database
            Task.objects.create(
                user=user,
                title=title,
                duration=duration,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )

            return Response({'message': 'Task created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, task_id):
        user_id = request.user.id
        new_title = request.data.get('title')
        if not new_title:
            return Response({'message': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE selteq_task SET title = %s WHERE user_id = %s AND id = %s",
                [new_title, user_id, task_id]
            )
            if cursor.rowcount > 0:
                return Response({'message': 'Task updated successfully'})
            return Response({'message': 'No task found for the given id'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, task_id):
        user_id = request.user.id
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM selteq_task WHERE user_id = %s AND id = %s",
                [user_id, task_id]
            )
            if cursor.rowcount > 0:
                return Response({'message': 'Task deleted successfully'})
            return Response({'message': 'No task found for the given id'}, status=status.HTTP_404_NOT_FOUND)

  

    
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        tasks = Task.objects.filter(user=user).order_by('-created_at')[:4]
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
