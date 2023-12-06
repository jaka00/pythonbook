from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import *


class StudentsView(APIView):
    def get(self, request, *args, **kwargs):
        students_list = Student.objects.all()
        serializer = StudentsSerializer(students_list, many=True)
        return Response(serializer.data)
    