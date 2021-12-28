from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Courses
from courses.serializers import CourseListSerializer


# Create your views here.

@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)