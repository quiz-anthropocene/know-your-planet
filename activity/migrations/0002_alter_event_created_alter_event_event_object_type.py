# Generated by Django 4.1 on 2022-08-17 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activity", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date de création"),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_object_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("QUESTION", "Question"),
                    ("QUIZ", "Quiz"),
                    ("USER", "Contributeur"),
                    ("WEEKLY_AGG_STAT", "Statistiques de la semaine"),
                ],
                max_length=50,
                verbose_name="Type d'objet",
            ),
        ),
    ]
