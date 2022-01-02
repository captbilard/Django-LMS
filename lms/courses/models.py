from django.db import models

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

    class Meta:
        verbose_name_plural = "Courses"
    
    def __str__(self):
        return self.title


class Lessons(models.Model):
    DRAFT = 'Draft'
    PUBLISHED = 'Published'

    LESSON_STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    ]

    ARTICLE = 'Article'
    QUIZ = 'Quiz'

    LESSON_TYPE_CHOICES = [
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
    ]

    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=LESSON_STATUS_CHOICES, default=PUBLISHED)
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPE_CHOICES, default=ARTICLE)

    class Meta:
        verbose_name_plural = "Lessons"
    
    def __str__(self):
        return self.title