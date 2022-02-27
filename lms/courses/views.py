import stripe

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import serializers, status

from .models import Courses, Lessons, Comments, Categories, Quiz
from courses.serializers import (
    CommentsSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    LessonListSerializer,
    CategoriesSerializer,
    QuizSerializer,
)


# Create your views here.


@api_view(["GET"])
@permission_classes([AllowAny])
def get_categories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_courses(request):
    category_id = request.GET.get("category_id", "")
    courses = Courses.objects.all()
    if category_id != "":
        courses = courses.filter(category__id=category_id)
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_front_page_courses(request):
    courses = Courses.objects.all()[0:4]
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_individual_course(request, slug):
    course = Courses.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    # lessons_serializer = LessonListSerializer(course.lessons.all(), many=True)
    if request.user.is_authenticated and request.user.has_perm("courses.premium_user"):
        lessons_serializer = LessonListSerializer(course.lessons.all(), many=True)
        course_data = course_serializer.data
        lessons_data = lessons_serializer.data
    elif request.user.is_authenticated and not request.user.has_perm(
        "courses.premium_user"
    ):
        lessons_serializer = LessonListSerializer(course.lessons.all()[0:2], many=True)
        course_data = course_serializer.data
        lessons_data = lessons_serializer.data
    else:
        course_data = {}
        lessons_data = {}
    data = {
        "course": course_data,
        "lessons": lessons_data,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_comment(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    comments_serializer = CommentsSerializer(lesson.comments.all(), many=True)
    return Response(comments_serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get("name")
    content = data.get("content")
    course = Courses.objects.get(slug=course_slug)
    lesson = Lessons.objects.get(slug=lesson_slug)
    created_by = request.user

    comment = Comments.objects.create(
        name=name, content=content, course=course, lesson=lesson, created_by=created_by
    )
    serializer = CommentsSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lessons.objects.get(slug=lesson_slug)
    serializer = QuizSerializer(lesson.quiz.first())
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_publishable_key(request):
    stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
    return Response(stripe_config, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def create_checkout_session(request):
    domain_url = "http://localhost:8081"
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=f"{domain_url}/success",
            cancel_url=f"{domain_url}/cancelled/",
            mode="payment",
            line_items=[
                {
                    "name": "Premium User",
                    "amount": "100",
                    "quantity": 1,
                    "currency": "usd",
                }
            ],
            payment_method_types=["card", "alipay"],
        )
        return Response({"session_id": checkout_session["id"]})
    except Exception as e:
        return Response({"error": str(e)})

@api_view(['GET'])
def make_user_premium(request):
    try:
        user = request.user
        premium_group = Group.objects.get(name="Premium Users")
        user.groups.add(premium_group)
        return Response({"msg":"Added to group"})
    except Exception as e:
        return Response({"error": str(e)})