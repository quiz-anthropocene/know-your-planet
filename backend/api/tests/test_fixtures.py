from django.core import management
from django.test import TestCase

from api.models import Category, Glossary, Question, Quiz, QuizRelationship, Tag
from core.models import Configuration


class FixturesTest(TestCase):
    # fixtures = [
    #     "data/categories.yaml",
    #     "data/tags.yaml",
    #     "data/questions.yaml",
    #     "data/quizzes.yaml",
    #     "data/quiz-relationships.yaml",
    #     "data/ressources-glossaire.yaml",
    # ]

    # def test_fixtures_load_successfully(self):
    #     self.assertTrue(Category.objects.count())
    #     self.assertTrue(Tag.objects.count())
    #     self.assertTrue(Question.objects.count())
    #     self.assertTrue(Quiz.objects.count())
    #     self.assertTrue(QuizRelationship.objects.count())
    #     self.assertTrue(Glossary.objects.count())

    def test_flat_fixtures_load_successfully(self):
        management.call_command("init_db")
        self.assertTrue(Configuration.objects.count())
        self.assertTrue(Category.objects.count())
        self.assertTrue(Tag.objects.count())
        self.assertTrue(Question.objects.count())
        self.assertTrue(Quiz.objects.count())
        self.assertTrue(QuizRelationship.objects.count())
        self.assertTrue(Glossary.objects.count())
