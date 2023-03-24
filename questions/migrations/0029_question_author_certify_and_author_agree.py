# Generated by Django 4.1.5 on 2023-03-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0028_alter_historicalquestion_history_changed_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalquestion",
            name="author_agree_commercial_use",
            field=models.BooleanField(default=True, verbose_name="I agree to the commercial use of this content"),
        ),
        migrations.AddField(
            model_name="historicalquestion",
            name="author_certify_necessary_rights",
            field=models.BooleanField(
                default=True,
                verbose_name="I certify that I have the necessary rights to publish and share this content",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="author_agree_commercial_use",
            field=models.BooleanField(default=True, verbose_name="I agree to the commercial use of this content"),
        ),
        migrations.AddField(
            model_name="question",
            name="author_certify_necessary_rights",
            field=models.BooleanField(
                default=True,
                verbose_name="I certify that I have the necessary rights to publish and share this content",
            ),
        ),
    ]
