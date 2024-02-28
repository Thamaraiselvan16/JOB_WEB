# Generated by Django 4.2.7 on 2024-01-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0005_job_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="experience",
            field=models.CharField(
                choices=[
                    ("Fresher", "Fresher"),
                    ("Less than 1 year", "Less than 1 year"),
                    ("1-3 years", "1-3 years"),
                    ("3-5 years", "3-5 years"),
                    ("5-10 years", "5-10 years"),
                    ("10+ years", "10+ years"),
                ],
                default="Fresher",
                max_length=20,
            ),
        ),
    ]
