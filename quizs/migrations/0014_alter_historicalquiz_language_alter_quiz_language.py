# Generated by Django 4.1a1 on 2022-07-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizs", "0013_historicalquiz_history_changed_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalquiz",
            name="language",
            field=models.CharField(
                choices=[("Français", "Français"), ("English", "English"), ("Deutsch", "Deutsch")],
                default="Français",
                max_length=50,
                verbose_name="Langue",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="language",
            field=models.CharField(
                choices=[("Français", "Français"), ("English", "English"), ("Deutsch", "Deutsch")],
                default="Français",
                max_length=50,
                verbose_name="Langue",
            ),
        ),
    ]
