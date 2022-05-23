# Generated by Django 4.1a1 on 2022-05-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizs", "0011_quizrelationship_updated"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalquiz",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Quiz",
                "verbose_name_plural": "historical Quizs",
            },
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]