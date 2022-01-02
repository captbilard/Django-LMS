# Generated by Django 4.0 on 2022-01-02 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_categories_short_description_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Published', max_length=15)),
                ('lesson_type', models.CharField(choices=[('Article', 'Article'), ('Quiz', 'Quiz')], default='Article', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='courses.courses')),
            ],
            options={
                'verbose_name_plural': 'Lessons',
            },
        ),
    ]