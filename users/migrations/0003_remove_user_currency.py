# Generated by Django 4.1 on 2024-10-13 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="currency",
        ),
    ]
