# Generated by Django 4.1.5 on 2023-02-23 10:11

import django.utils.timezone
from django.db import migrations, models

import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_created"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "User", "verbose_name_plural": "Users"},
        ),
        migrations.AlterField(
            model_name="user",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Email"),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="roles",
            field=core.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("CONTRIBUTOR", "Contributor"),
                        ("SUPER-CONTRIBUTOR", "Super Contributor"),
                        ("ADMINISTRATOR", "Administrator"),
                    ],
                    max_length=20,
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Roles",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
    ]