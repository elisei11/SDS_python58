# Generated by Django 5.0.6 on 2024-06-23 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feedback",
            name="dummy_field",
        ),
    ]
