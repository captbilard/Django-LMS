from django.db.models import fields
from rest_framework import serializers
from .models import Comments, Courses, Lessons, Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('title', 'slug')

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','slug', 'short_description', 'get_image')

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','slug', 'short_description', 'long_description')

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ('id','title','slug', 'short_description', 'long_description')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','name','content','created_at')