# Generated by Django 4.2.7 on 2024-02-20 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_tag_remove_task_vacancy_remove_taskvalue_task_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="specialization",
            name="tags",
        ),
        migrations.AddField(
            model_name="tag",
            name="specialization",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, related_name="tags", to="main.specialization"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="tags",
            field=models.ManyToManyField(blank=True, related_name="vacancies", to="main.tag"),
        ),
    ]