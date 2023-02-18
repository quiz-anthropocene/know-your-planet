# Generated by Django 4.1.5 on 2023-02-18 19:54

from django.db import migrations


def migrate_question_language(apps, schema_editor):
    Question = apps.get_model("questions", "Question")
    Question.objects.filter(language="Français").update(language="FRENCH")
    Question.objects.filter(language="English").update(language="ENGLISH")
    Question.objects.filter(language="Deutsch").update(language="GERMAN")


def migrate_historical_question_language(apps, schema_editor):
    HistoricalQuestion = apps.get_model("questions", "HistoricalQuestion")
    HistoricalQuestion.objects.filter(language="Français").update(language="FRENCH")
    HistoricalQuestion.objects.filter(language="English").update(language="ENGLISH")
    HistoricalQuestion.objects.filter(language="Deutsch").update(language="GERMAN")


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0021_alter_historicalquestion_answer_audio_url_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate_question_language),
        migrations.RunPython(migrate_historical_question_language),
    ]
