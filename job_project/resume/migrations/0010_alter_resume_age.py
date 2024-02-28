# Generated by Django 4.2.7 on 2024-01-11 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0009_resume_current_position_resume_phone_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="age",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(
                        limit_value=98, message="Age must be less than 99."
                    )
                ],
            ),
        ),
    ]