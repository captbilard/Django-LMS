# from django.test import TestCase
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Courses, Lessons, Comments, Categories, Quiz
from courses.serializers import (
    CommentsSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    LessonListSerializer,
    CategoriesSerializer,
    QuizSerializer,
)

# Create your tests here.

class CoursesTest(APITestCase):
    def setUp(self):
        self.category = Categories.objects.create(title="design", slug="design-course")
        self.course = Courses.objects.create(title="The design course",slug="the-design-course")
        self.course.category.add(self.category)

    def test_get_categories(self):
        """
        Ensures that the endpoints returns 
        all categories
        """
        url = reverse("get_categories")
        serializer = CategoriesSerializer(Categories.objects.all(), many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_get_courses(self):
        """
        Ensures that the endpoints returns 
        all courses
        """
        url = reverse("get_courses")
        serializer = CourseListSerializer(Courses.objects.all(), many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

