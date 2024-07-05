# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if username and password:
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
        raise serializers.ValidationError("Incorrect Credentials")
class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    duration = serializers.DurationField()