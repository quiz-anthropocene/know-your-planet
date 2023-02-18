# Generated by Django 4.1.5 on 2023-02-19 10:35

import django.contrib.postgres.fields
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quizs", "0024_alter_historicalquiz_validation_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalquiz",
            name="author_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50), blank=True, default=list, size=None, verbose_name="Authors"
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="difficulty_average",
            field=models.FloatField(default=0, verbose_name="Average difficulty level"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="has_audio",
            field=models.BooleanField(default=False, verbose_name="Audio answers?"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="image_background_url",
            field=models.URLField(blank=True, max_length=500, verbose_name="Background image (link)"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="language",
            field=models.CharField(
                choices=[("FRENCH", "French"), ("ENGLISH", "English"), ("GERMAN", "German")],
                default="FRENCH",
                max_length=50,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="publish",
            field=models.BooleanField(default=False, verbose_name="Published?"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="publish_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Publication date"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="relationship_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                blank=True,
                default=list,
                size=None,
                verbose_name="Relationships",
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="slug",
            field=models.SlugField(verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="spotlight",
            field=models.BooleanField(default=False, verbose_name="Spotlighted?"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="updated",
            field=models.DateTimeField(blank=True, editable=False, verbose_name="Last update date"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="validation_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Validation date"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="validation_status",
            field=models.CharField(
                choices=[
                    ("DRAFT", "Draft"),
                    ("TO_VALIDATE", "To validate"),
                    ("VALIDATED", "Validated"),
                    ("ASIDE", "Set aside"),
                    ("REMOVED", "Removed"),
                ],
                default="DRAFT",
                max_length=150,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="validator",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Validator",
            ),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="validator_string",
            field=models.CharField(blank=True, max_length=300, verbose_name="Validator"),
        ),
        migrations.AlterField(
            model_name="historicalquiz",
            name="visibility",
            field=models.CharField(
                choices=[
                    ("PUBLIC", "Public (exported and the application)"),
                    ("HIDDEN", "Hidden (exported but not visible in the application)"),
                    ("PRIVATE", "Private (not exported and not in the application)"),
                ],
                default="PUBLIC",
                max_length=50,
                verbose_name="Visibility",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="author_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50), blank=True, default=list, size=None, verbose_name="Authors"
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="authors",
            field=models.ManyToManyField(
                blank=True,
                related_name="quizs",
                through="quizs.QuizAuthor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Authors",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="difficulty_average",
            field=models.FloatField(default=0, verbose_name="Average difficulty level"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="has_audio",
            field=models.BooleanField(default=False, verbose_name="Audio answers?"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="image_background_url",
            field=models.URLField(blank=True, max_length=500, verbose_name="Background image (link)"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="language",
            field=models.CharField(
                choices=[("FRENCH", "French"), ("ENGLISH", "English"), ("GERMAN", "German")],
                default="FRENCH",
                max_length=50,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="publish",
            field=models.BooleanField(default=False, verbose_name="Published?"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="publish_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Publication date"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="relationship_list",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                blank=True,
                default=list,
                size=None,
                verbose_name="Relationships",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="relationships",
            field=models.ManyToManyField(
                related_name="related_to",
                through="quizs.QuizRelationship",
                to="quizs.quiz",
                verbose_name="Similar or related quizs",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="spotlight",
            field=models.BooleanField(default=False, verbose_name="Spotlighted?"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="validation_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Validation date"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="validation_status",
            field=models.CharField(
                choices=[
                    ("DRAFT", "Draft"),
                    ("TO_VALIDATE", "To validate"),
                    ("VALIDATED", "Validated"),
                    ("ASIDE", "Set aside"),
                    ("REMOVED", "Removed"),
                ],
                default="DRAFT",
                max_length=150,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="validator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="quizs_validated",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Validator",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="validator_string",
            field=models.CharField(blank=True, max_length=300, verbose_name="Validator"),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="visibility",
            field=models.CharField(
                choices=[
                    ("PUBLIC", "Public (exported and the application)"),
                    ("HIDDEN", "Hidden (exported but not visible in the application)"),
                    ("PRIVATE", "Private (not exported and not in the application)"),
                ],
                default="PUBLIC",
                max_length=50,
                verbose_name="Visibility",
            ),
        ),
        migrations.AlterField(
            model_name="quizauthor",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Author"
            ),
        ),
        migrations.AlterField(
            model_name="quizauthor",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="quizauthor",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
        migrations.AlterField(
            model_name="quizquestion",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="quizquestion",
            name="order",
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name="Order"),
        ),
        migrations.AlterField(
            model_name="quizquestion",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
        migrations.AlterField(
            model_name="quizrelationship",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date"),
        ),
        migrations.AlterField(
            model_name="quizrelationship",
            name="status",
            field=models.CharField(
                choices=[
                    ("suivant", "suivant"),
                    ("jumeau", "jumeau"),
                    ("similaire", "similaire"),
                    ("traduction", "traduction"),
                ],
                max_length=50,
                verbose_name="Relationship type",
            ),
        ),
        migrations.AlterField(
            model_name="quizrelationship",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Last update date"),
        ),
    ]
