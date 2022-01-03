from django.db.models import fields
from rest_framework import serializers
from .models import Comments, Courses, Lessons

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','slug', 'short_description',)

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','slug', 'short_description', 'long_description')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id','title','slug', 'short_description', 'long_description')
