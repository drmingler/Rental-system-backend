# Generated by Django 3.1.7 on 2021-03-28 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_auto_20210328_1901"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthDate",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                max_length=128,
                verbose_name="Birth date",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
