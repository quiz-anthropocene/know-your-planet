# Generated by Django 3.2.7 on 2021-10-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0083_quiz_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(help_text="Le bout d'url du quiz", unique=True),
        ),
    ]
