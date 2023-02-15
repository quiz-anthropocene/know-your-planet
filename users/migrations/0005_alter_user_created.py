# Generated by Django 4.1 on 2022-08-17 14:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_timestamps"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date de création"),
        ),
    ]