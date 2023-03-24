# Generated by Django 4.1.5 on 2023-03-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contributions", "0016_comment_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "To process"),
                    ("PENDING", "In progress"),
                    ("PROCESSED", "Processed"),
                    ("IGNORED", "Ignored"),
                ],
                default="NEW",
                max_length=150,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomment",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "To process"),
                    ("PENDING", "In progress"),
                    ("PROCESSED", "Processed"),
                    ("IGNORED", "Ignored"),
                ],
                default="NEW",
                max_length=150,
                verbose_name="Status",
            ),
        ),
    ]
