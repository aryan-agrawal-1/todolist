# Generated by Django 5.0.3 on 2024-03-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todos",
            name="isDone",
            field=models.BooleanField(default=False),
        ),
    ]
