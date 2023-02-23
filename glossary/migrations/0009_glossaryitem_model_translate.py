# Generated by Django 4.1.5 on 2023-02-23 13:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glossary", "0008_alter_historicalglossaryitem_history_changed_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glossaryitem",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="glossaryitem",
            name="definition_short",
            field=models.CharField(max_length=150, verbose_name="Définition (short)"),
        ),
        migrations.AlterField(
            model_name="glossaryitem",
            name="description_accessible_url",
            field=models.URLField(blank=True, max_length=500, verbose_name="Accessible source (link)"),
        ),
        migrations.AlterField(
            model_name="glossaryitem",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Word or acronym"),
        ),
        migrations.AlterField(
            model_name="glossaryitem",
            name="name_alternatives",
            field=models.TextField(blank=True, verbose_name="Alternative names"),
        ),
        migrations.AlterField(
            model_name="glossaryitem",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="definition_short",
            field=models.CharField(max_length=150, verbose_name="Définition (short)"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="description_accessible_url",
            field=models.URLField(blank=True, max_length=500, verbose_name="Accessible source (link)"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Word or acronym"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="name_alternatives",
            field=models.TextField(blank=True, verbose_name="Alternative names"),
        ),
        migrations.AlterField(
            model_name="historicalglossaryitem",
            name="updated",
            field=models.DateTimeField(blank=True, editable=False, verbose_name="Last update date"),
        ),
    ]
