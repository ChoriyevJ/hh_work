# Generated by Django 4.2.7 on 2024-02-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_rename_skills_skill"),
    ]

    operations = [
        migrations.AddField(
            model_name="vacancy",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
    ]