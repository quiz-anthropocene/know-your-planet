# Generated by Django 3.2.7 on 2021-10-24 15:46

from django.db import migrations, models
from django.utils.text import slugify


def slugify_name(apps, schema_editor):
    # see Quiz.set_slug()
    Quiz = apps.get_model("api", "Quiz")
    for quiz in Quiz.objects.all():
        quiz.slug = slugify(quiz.name)
        quiz.save()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0082_delete_configuration"),
    ]

    operations = [
        migrations.AddField(
            model_name="quiz",
            name="slug",
            field=models.SlugField(help_text="Le bout d'url du quiz", null=True),
        ),
        migrations.RunPython(slugify_name),
    ]
