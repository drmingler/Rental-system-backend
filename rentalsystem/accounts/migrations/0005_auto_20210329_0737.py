# Generated by Django 3.1.7 on 2021-03-29 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20210328_1938"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="updated_at",
        ),
    ]
