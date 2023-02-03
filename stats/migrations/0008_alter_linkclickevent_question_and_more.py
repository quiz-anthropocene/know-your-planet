# Generated by Django 4.1.5 on 2023-02-03 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0017_rename_answer_audio_historicalquestion_answer_audio_url_and_more"),
        ("quizs", "0020_remove_historicalquiz_author_and_more"),
        ("stats", "0007_linkclickevent_field_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="linkclickevent",
            name="question",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="link_clicks",
                to="questions.question",
            ),
        ),
        migrations.AlterField(
            model_name="linkclickevent",
            name="quiz",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="link_clicks",
                to="quizs.quiz",
            ),
        ),
    ]
