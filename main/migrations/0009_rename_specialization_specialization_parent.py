# Generated by Django 4.2.7 on 2024-02-21 08:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_vacancy_publish_type_vacancy_published_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="specialization",
            old_name="specialization",
            new_name="parent",
        ),
    ]