from django.contrib import admin

from .models import Categories, Courses

# Register your models here.
admin.site.register(Categories)
admin.site.register(Courses)