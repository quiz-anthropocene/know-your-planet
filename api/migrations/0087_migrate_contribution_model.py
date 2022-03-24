# Generated by Django 4.0.3 on 2022-03-24 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0086_model_verbose_names"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Contribution",
                ),
            ],
            # want to reuse the table, don't drop it
            database_operations=[
                migrations.AlterModelTable(
                    name="Contribution",
                    table="contributions_contribution",
                )
            ],
        )
    ]
