# Generated by Django 4.1.4 on 2023-03-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_livesession_pub_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livesession",
            name="duration",
        ),
    ]
