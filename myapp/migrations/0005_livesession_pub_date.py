# Generated by Django 4.1.4 on 2023-03-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_currentnews_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="livesession",
            name="pub_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
