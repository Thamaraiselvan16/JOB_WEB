# Generated by Django 4.2.7 on 2024-01-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0007_resume_skills"),
    ]

    operations = [
        migrations.AddField(
            model_name="resume",
            name="experience",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
