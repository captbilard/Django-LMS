from django.contrib import admin

from .models import Categories, Courses, Lessons

# Register your models here.
admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Lessons)