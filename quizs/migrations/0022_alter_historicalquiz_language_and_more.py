# Generated by Django 4.1.5 on 2023-02-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizs", "0021_quiz_language_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalquiz",
            name="language",
            field=models.CharField(
                choices=[("FRENCH", "French"), ("ENGLISH", "English"), ("GERMAN", "German")],
                default="FRENCH",
                max_length=50,
                verbose_name="Langue",
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="visibility",
            field=models.CharField(
                choices=[
                    ("PUBLIC", "Public (exported and the application)"),
                    ("HIDDEN", "Hidden (exported but not visible in the application)"),
                    ("PRIVATE", "Private (not exported and not in the application)"),
                ],
                default="PUBLIC",
                max_length=50,
                verbose_name="Visibilité",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="language",
            field=models.CharField(
                choices=[("FRENCH", "French"), ("ENGLISH", "English"), ("GERMAN", "German")],
                default="FRENCH",
                max_length=50,
                verbose_name="Langue",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="visibility",
            field=models.CharField(
                choices=[
                    ("PUBLIC", "Public (exported and the application)"),
                    ("HIDDEN", "Hidden (exported but not visible in the application)"),
                    ("PRIVATE", "Private (not exported and not in the application)"),
                ],
                default="PUBLIC",
                max_length=50,
                verbose_name="Visibilité",
            ),
        ),
    ]
