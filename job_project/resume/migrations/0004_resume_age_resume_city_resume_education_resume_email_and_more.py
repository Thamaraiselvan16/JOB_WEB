# Generated by Django 4.2.7 on 2024-01-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0003_rename_surname_resume_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="education",
            field=models.CharField(
                blank=True,
                choices=[
                    ("high_school", "High School"),
                    ("associate_degree", "Associate Degree"),
                    ("bachelor_degree", "Bachelor's Degree"),
                    ("master_degree", "Master's Degree"),
                    ("doctorate", "Doctorate"),
                    ("other", "Other"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="resume",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="resume",
            name="state",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
