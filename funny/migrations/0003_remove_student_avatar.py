# Generated by Django 4.1.5 on 2023-01-19 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funny', '0002_alter_student_options_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='avatar',
        ),
    ]
