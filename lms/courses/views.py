from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status

from .models import Courses, Lessons
from courses.serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer


# Create your views here.

@api_view(['GET'])
def get_courses(request):
    courses = Courses.objects.all()
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_individual_course(request, slug):
    course = Courses.objects.get(slug=slug)
    serializer = CourseDetailSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)
