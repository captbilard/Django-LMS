# from django.test import TestCase
import json
from unicodedata import category
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
        Categories.objects.create(title="design", slug="design-course")
    def test_get_categories(self):
        """
        Ensures that the endpoints returns 
        all categories
        """
        url = reverse("get_categories")
        serializer = CategoriesSerializer(Categories.objects.all(), many=True)
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

