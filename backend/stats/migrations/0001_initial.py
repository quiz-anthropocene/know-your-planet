# Generated by Django 4.0.3 on 2022-03-30 22:31

import django.db.models.deletion
from django.db import migrations, models

import stats.constants


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("questions", "0001_initial"),
        ("quizs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DailyStat",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(help_text="Le jour de la statistique")),
                (
                    "question_answer_count",
                    models.PositiveIntegerField(default=0, help_text="Le nombre de questions répondues"),
                ),
                (
                    "question_answer_from_quiz_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Le nombre de questions répondues au sein de quizs"
                    ),
                ),
                ("quiz_answer_count", models.PositiveIntegerField(default=0, help_text="Le nombre de quizs répondus")),
                (
                    "question_feedback_count",
                    models.PositiveIntegerField(default=0, help_text="Le nombre de feedbacks aux questions"),
                ),
                (
                    "question_feedback_from_quiz_count",
                    models.PositiveIntegerField(
                        default=0, help_text="Le nombre de feedbacks aux questions au sein de quizs"
                    ),
                ),
                (
                    "quiz_feedback_count",
                    models.PositiveIntegerField(default=0, help_text="Le nombre de feedbacks aux quizs"),
                ),
                (
                    "hour_split",
                    models.JSONField(
                        default=stats.constants.daily_stat_hour_split_jsonfield_default_value,
                        help_text="Les statistiques par heure",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, help_text="La date & heure de la stat journalière"),
                ),
                ("updated", models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionAggStat",
            fields=[
                (
                    "question",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="agg_stats",
                        serialize=False,
                        to="questions.question",
                    ),
                ),
                ("answer_count", models.PositiveIntegerField(default=0, help_text="Le nombre de réponses")),
                (
                    "answer_success_count",
                    models.PositiveIntegerField(default=0, help_text="Le nombre de réponses correctes"),
                ),
                ("like_count", models.PositiveIntegerField(default=0, help_text="Le nombre de likes")),
                ("dislike_count", models.PositiveIntegerField(default=0, help_text="Le nombre de dislikes")),
            ],
        ),
        migrations.CreateModel(
            name="QuizAggStat",
            fields=[
                (
                    "quiz",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="agg_stats",
                        serialize=False,
                        to="quizs.quiz",
                    ),
                ),
                ("answer_count", models.PositiveIntegerField(default=0, help_text="Le nombre de réponses")),
                ("like_count", models.PositiveIntegerField(default=0, help_text="Le nombre de likes")),
                ("dislike_count", models.PositiveIntegerField(default=0, help_text="Le nombre de dislikes")),
            ],
        ),
        migrations.CreateModel(
            name="QuizFeedbackEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "choice",
                    models.CharField(
                        choices=[("like", "Positif"), ("dislike", "Négatif")],
                        default="like",
                        help_text="L'avis laissé sur le quiz",
                        max_length=50,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, help_text="La date & heure de l'avis")),
                (
                    "quiz",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="quizs.quiz",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuizAnswerEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question_count", models.IntegerField(default=0, help_text="La nombre de questions du quiz")),
                (
                    "answer_success_count",
                    models.IntegerField(
                        default=0, help_text="La nombre de réponses correctes trouvées par l'internaute"
                    ),
                ),
                (
                    "duration_seconds",
                    models.IntegerField(default=0, help_text="Le temps pris (en secondes) pour compléter le quiz"),
                ),
                ("created", models.DateTimeField(auto_now_add=True, help_text="La date & heure de la réponse")),
                (
                    "quiz",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, related_name="stats", to="quizs.quiz"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionFeedbackEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "choice",
                    models.CharField(
                        choices=[("like", "Positif"), ("dislike", "Négatif")],
                        default="like",
                        help_text="L'avis laissé sur la question",
                        max_length=50,
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[("question", "Question"), ("quiz", "Quiz")],
                        default="question",
                        help_text="Le contexte dans lequel a été envoyé l'avis",
                        max_length=50,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, help_text="La date & heure de l'avis")),
                (
                    "question",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="questions.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuestionAnswerEvent",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "choice",
                    models.CharField(
                        choices=[
                            ("a", "a"),
                            ("b", "b"),
                            ("c", "c"),
                            ("d", "d"),
                            ("ab", "ab"),
                            ("ac", "ac"),
                            ("ad", "ad"),
                            ("bc", "bc"),
                            ("bd", "bd"),
                            ("cd", "cd"),
                            ("abc", "abc"),
                            ("abd", "abd"),
                            ("acd", "acd"),
                            ("bcd", "bcd"),
                            ("abcd", "abcd"),
                        ],
                        help_text="La réponse choisie par l'internaute",
                        max_length=50,
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[("question", "Question"), ("quiz", "Quiz")],
                        default="question",
                        help_text="Le contexte dans lequel a été répondu la question",
                        max_length=50,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, help_text="La date & heure de la réponse")),
                (
                    "question",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats",
                        to="questions.question",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="dailystat",
            constraint=models.UniqueConstraint(fields=("date",), name="stat_date_unique"),
        ),
    ]
