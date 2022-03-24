# Generated by Django 3.1.1 on 2020-12-02 00:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0059_question_validation_status_aside"),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="application_about",
            field=ckeditor.fields.RichTextField(blank=True, help_text="A propos de l'application"),
        ),
        migrations.AddField(
            model_name="configuration",
            name="application_tagline",
            field=models.CharField(default="", help_text="La tagline de l'application", max_length=255),
            preserve_default=False,
        ),
    ]
