from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Courses(models.Model):
    category = models.ManyToManyField(Categories)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    # price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Courses"
        permissions = [
            ('premium_user', "Can access all lessons")
        ]

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return f"{settings.WEBSITE_URL}{self.image.url}"
        else:
            return f"https://bulma.io/images/placeholders/1280x960.png"


class Lessons(models.Model):
    DRAFT = "Draft"
    PUBLISHED = "Published"

    LESSON_STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    ]

    ARTICLE = "Article"
    QUIZ = "Quiz"

    LESSON_TYPE_CHOICES = [
        (ARTICLE, "Article"),
        (QUIZ, "Quiz"),
    ]

    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="lessons"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=15, choices=LESSON_STATUS_CHOICES, default=PUBLISHED
    )
    lesson_type = models.CharField(
        max_length=10, choices=LESSON_TYPE_CHOICES, default=ARTICLE
    )

    class Meta:
        verbose_name_plural = "Lessons"
        ordering = ["id"]


class Comments(models.Model):
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name="comments"
    )
    lesson = models.ForeignKey(
        Lessons, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment on {self.lesson}"


class Quiz(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name="quiz")
    question = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = "Quizzes"
