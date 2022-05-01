# Generated by Django 4.0.4 on 2022-05-01 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contributions", "0003_add_verbose_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="contribution",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="contributions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Auteur",
            ),
        ),
    ]
