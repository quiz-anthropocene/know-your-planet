# Generated by Django 4.0.3 on 2022-03-24 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0087_migrate_contribution_model"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name="Glossary",
                ),
            ],
            # want to reuse the table, don't drop it
            database_operations=[
                migrations.AlterModelTable(
                    name="Glossary",
                    table="glossary_glossary",
                )
            ],
        )
    ]