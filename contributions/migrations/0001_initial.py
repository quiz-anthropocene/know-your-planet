# Generated by Django 4.0.3 on 2022-03-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Contribution",
                    fields=[
                        (
                            "id",
                            models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                        ),
                        (
                            "text",
                            models.TextField(
                                help_text="La contribution de l'utilisateur (une question ou un commentaire)"
                            ),
                        ),
                        (
                            "description",
                            models.TextField(
                                help_text="Informations supplémentaires sur la contribution (réponse, lien, ...)"
                            ),
                        ),
                        (
                            "type",
                            models.CharField(
                                blank=True,
                                choices=[
                                    ("nouvelle question", "nouvelle question"),
                                    ("nouveau quiz", "nouveau quiz"),
                                    ("commentaire application", "commentaire application"),
                                    ("commentaire question", "commentaire question"),
                                    ("commentaire quiz", "commentaire quiz"),
                                    ("nom application", "nom application"),
                                    ("erreur application", "erreur application"),
                                ],
                                help_text="Le type de contribution",
                                max_length=150,
                            ),
                        ),
                        (
                            "created",
                            models.DateTimeField(auto_now_add=True, help_text="La date & heure de la contribution"),
                        ),
                    ],
                ),
            ],
            # Table already exist, see api/migrations/0087_migrate_contribution_model.py
            database_operations=[],
        )
    ]
