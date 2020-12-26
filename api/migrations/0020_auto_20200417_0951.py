# Generated by Django 3.0.4 on 2020-04-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0019_questionstat_source"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="questioncategory",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique category name"
            ),
        ),
        migrations.AddConstraint(
            model_name="questiontag",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique tag name"
            ),
        ),
    ]
