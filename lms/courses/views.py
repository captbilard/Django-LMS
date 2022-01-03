from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status

from .models import Comments, Courses, Lessons
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
    course_serializer = CourseDetailSerializer(course)
    lessons_serializer = LessonListSerializer(course.lessons.all(), many=True)
    data = {
        "course": course_serializer.data,
        "lessons": lessons_serializer.data,
    }
    return Response(data, status=status.HTTP_200_OK)



@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.GET['name']
    content = data.GET['content']
    course = Courses.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)
    created_by = request.user

    Comments.objects.create(
        name=name, content=content,course=course,lesson=lesson,created_by=created_by
    )
    return Response({"message":"Comments added!"}, status=status.HTTP_201_CREATED)