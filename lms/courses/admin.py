from django.contrib import admin

from .models import Categories, Courses, Lessons, Comments, Quiz

# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comments
    raw_id_fields = ["lesson"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "status", "lesson_type")
    list_filter = ("status", "lesson_type")
    search_fields = ["title"]
    inlines = [CommentsInline]


admin.site.register(Categories)
admin.site.register(Courses)
admin.site.register(Lessons, LessonAdmin)
admin.site.register(Comments)
admin.site.register(Quiz)
