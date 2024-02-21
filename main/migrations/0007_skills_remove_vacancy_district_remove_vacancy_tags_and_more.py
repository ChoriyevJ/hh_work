# Generated by Django 4.2.7 on 2024-02-21 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0006_remove_specialization_tags_tag_specialization_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Skills",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="vacancy",
            name="district",
        ),
        migrations.RemoveField(
            model_name="vacancy",
            name="tags",
        ),
        migrations.AddField(
            model_name="region",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regions",
                to="main.region",
            ),
        ),
        migrations.AddField(
            model_name="specialization",
            name="specialization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="main.specialization",
            ),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="districts",
            field=models.ManyToManyField(related_name="vacancies", to="main.district"),
        ),
        migrations.AlterField(
            model_name="district",
            name="neighbour",
            field=models.ManyToManyField(blank=True, to="main.district"),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="experience",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="main.experience"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="price_type",
            field=models.CharField(
                blank=True, choices=[("SUM", "Sum"), ("DOLLAR", "$"), ("EURO", "€")], max_length=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="saved",
            field=models.ManyToManyField(blank=True, related_name="saved_vacancy", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="work_schedule",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FULL_DAY", "Полный день"),
                    ("SHIFT_SH", "Сменный график "),
                    ("REMOTE", "Удаленная работа"),
                    ("SHIFT_M", "Вахтовый метод"),
                    ("FLEXIBLE", "Гибкий график"),
                ],
                max_length=31,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.AddField(
            model_name="vacancy",
            name="skills",
            field=models.ManyToManyField(blank=True, related_name="vacancies", to="main.skills"),
        ),
    ]
