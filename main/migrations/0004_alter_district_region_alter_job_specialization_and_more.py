# Generated by Django 4.2.7 on 2024-02-20 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_specializationtype_job_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="district",
            name="region",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="districts", to="main.region"
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="specialization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="jobs", to="main.specialization"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="industry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="vacancies", to="main.industry"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="vacancies", to="main.job"
            ),
        ),
        migrations.AlterField(
            model_name="vacancy",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
