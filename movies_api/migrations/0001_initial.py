# Generated by Django 5.0.3 on 2024-03-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "protagonists",
                    models.CharField(blank=True, max_length=60, null=True),
                ),
                ("poster", models.URLField(blank=True, null=True)),
                ("trailer", models.URLField(blank=True, null=True)),
                ("start_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("coming-up", "Coming Up"),
                            ("starting", "Starting"),
                            ("running", "Running"),
                            ("finished", "Finished"),
                        ],
                        default="user",
                        max_length=60,
                    ),
                ),
                ("rank", models.IntegerField()),
            ],
        )
    ]
