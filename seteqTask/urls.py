"""seteqTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from selteq.views import UserLoginView, TokenRefreshView,TaskView, TaskListView,  UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('task/create/', TaskView.as_view(), name='task_create'),
    path('task/retrieve/<int:task_id>/', TaskView.as_view(), name='task_retrieve'),
    path('task/list/', TaskListView.as_view(), name='task_list'),
    path('task/update/<int:task_id>/', TaskView.as_view(), name='task_update'),
    path('task/delete/<int:task_id>/', TaskView.as_view(), name='task_delete'),
    
]

