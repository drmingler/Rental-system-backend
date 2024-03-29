# Generated by Django 3.1.7 on 2021-03-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_auto_20210329_0743"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthDate",
            field=models.DateTimeField(
                blank=True, max_length=128, null=True, verbose_name="Birth date"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="userType",
            field=models.CharField(
                blank=True,
                choices=[("Landlord", "Landlord"), ("Tenant", "Tenant")],
                default="Tenant",
                max_length=30,
                verbose_name="User type",
            ),
        ),
    ]
