from django.urls import path
from rest_framework import views

from .views import *

urlpatterns = [
    path('', get_courses, name="get_courses"),
    path('<slug:slug>/', get_individual_course, name="get_individual_course"),
    path('<slug:course_slug>/<slug:lesson_slug>/', add_comment, name="create_comment"),
]
