# Generated by Django 4.2.7 on 2024-01-10 07:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resume", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resume",
            old_name="surname",
            new_name="last_name",
        ),
    ]
