# Generated by Django 4.0 on 2022-02-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_courses_options_alter_quiz_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
    ]
