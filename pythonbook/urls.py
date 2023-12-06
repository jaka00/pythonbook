"""
URL configuration for pythonbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from task.views.task import *
from students.views import *
from students.serializers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/usersapp/", include("users.urls", namespace="usersapp")),
    path("api/task/", include("task.urls", namespace="task")),
    # path("api/answer/", include("task.urls", namespace="answer")),
    path('api/answer/detail/<int:pk>/', AnswerDetailAPIView.as_view(), name="answer-detail"),
    path('api/answer/list/', AnswersView.as_view(), name='list'),
    path('api/students/detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('api/students/list/', StudentsView.as_view(), name="list"),
]