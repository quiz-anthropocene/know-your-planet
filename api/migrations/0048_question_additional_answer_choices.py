# Generated by Django 3.0.4 on 2020-09-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0047_auto_20200911_1830"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="answer_correct",
            field=models.CharField(
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
                help_text="a, b, c ou d. ab, acd, abcd, etc si plusieurs réponses.",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="questionanswerevent",
            name="choice",
            field=models.CharField(
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
                editable=False,
                help_text="La réponse choisie par l'internaute",
                max_length=50,
            ),
        ),
    ]
