from django.urls import path
from .views import *

app_name = 'students'

urlpatterns = [
    path('list/', StudentsView.as_view(), name='list'),
]