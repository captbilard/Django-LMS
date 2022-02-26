from django.urls import path
from rest_framework import views

from .views import *

urlpatterns = [
    path('', get_courses, name="get_courses"),
    path('get_publishable_key/', get_publishable_key, name="get_publishable_key"),
    path('get_frontpage_courses/', get_front_page_courses, name="get_frontpage_courses"),
    path('get_categories/', get_categories, name="get_categories"),
    path('<slug:slug>/', get_individual_course, name="get_individual_course"),
    path('<slug:course_slug>/<slug:lesson_slug>/', add_comment, name="add_comment"),
    path("<slug:course_slug>/<slug:lesson_slug>/get-comments/", get_comment, name="get_comment"),
    path("<slug:course_slug>/<slug:lesson_slug>/get-quiz/", get_quiz, name="get_quiz"),
]
