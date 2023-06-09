# Generated by Django 4.1.4 on 2023-03-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LiveSession",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("speaker", models.CharField(max_length=200)),
                ("datetime", models.DateField()),
                ("duration", models.DurationField()),
                ("youtubeLink", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
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
                ("headline", models.CharField(max_length=200)),
                ("headlineLink", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("pub_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
