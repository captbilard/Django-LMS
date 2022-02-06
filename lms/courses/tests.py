# from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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
        # User authentication
        self.user = User.objects.create_user(username="test@example.com", email="test@example.com", password="Testpass123*")
        self.user.save()
        token = Token.objects.create(user=self.user)
        token.save()

        self.category = Categories.objects.create(title="design", slug="design-course")
        self.course = Courses.objects.create(title="The design course",slug="the-design-course")
        self.course1 = Courses.objects.create(title="Course1",slug="course-1")
        self.course2 = Courses.objects.create(title="Course2",slug="course-2")
        self.course3 = Courses.objects.create(title="Course3",slug="course-3")
        self.course4 = Courses.objects.create(title="Course4",slug="course-4")
        self.course.category.add(self.category)
        self.course1.category.add(self.category)
        self.course2.category.add(self.category)
        self.course3.category.add(self.category)
        self.course4.category.add(self.category)
        self.lesson = Lessons.objects.create(course=self.course, title="Design-lesson", slug="design-lesson")


    def _require_login(self):
        # Logs the user in
        self.client.login(username="test@example.com", password="Testpass123*")
    

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

    def test_get_frontpage_courses(self):
        """
        Ensures only the top 4 courses is returned 
        """
        url = reverse("get_frontpage_courses")
        serializer = CourseListSerializer(Courses.objects.all()[0:4], many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(response.data, serializer.data)
    
    def test_get_individual_course(self):
        """
        Get course details
        """
        self._require_login()
        url = reverse("get_individual_course", kwargs={'slug':self.course.slug})
        course_serializer = CourseDetailSerializer(self.course)
        lessons_serializer = LessonListSerializer(self.course.lessons.all(), many=True)
        data = {
            "course": course_serializer.data,
            "lessons": lessons_serializer.data,
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    
    def test_add_comment(self):
        """
        Add comments to a lesson
        """
        self._require_login()
        url = reverse("add_comment", kwargs={'course_slug':self.course.slug, 'lesson_slug':self.lesson.slug})
        data = {'course':self.course.id, 'lesson':self.lesson.id, 'name':"Test_user",'content':'This is a test comment', 'created_by':self.user.username}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comments.objects.count(), 1)
        self.assertEqual(Comments.objects.get().name, 'Test_user')
    
    def test_get_comment(self):
        """
        Get comments from a lesson
        """
        self._require_login()
        url = reverse("get_comment", kwargs={'course_slug':self.course.slug, 'lesson_slug':self.lesson.slug})
        serializer = CommentsSerializer(self.lesson.comments.all(), many=True)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(response.data, serializer.data)
        
