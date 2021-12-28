from django.db.models import fields
from rest_framework import serializers
from .models import Courses

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id','title','slug', 'short_description',)