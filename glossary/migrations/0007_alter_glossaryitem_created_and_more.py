# Generated by Django 4.1 on 2022-08-17 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glossary", "0006_historicalglossaryitem_history_changed_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glossaryitem",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date de création"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date de création"),
        ),
    ]
