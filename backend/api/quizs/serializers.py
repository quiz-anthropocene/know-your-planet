from rest_framework import serializers

from api.questions.serializers import QuestionSerializer
from api.tags.serializers import TagSerializer
from quizs.models import Quiz, QuizQuestion


class QuizQuestionSerializer(serializers.ModelSerializer):
    # override QuizQuestion id with question_id
    id = serializers.ReadOnlyField(source="question.id")

    class Meta:
        model = QuizQuestion
        fields = ["id", "order"]


QUIZ_FIELDS = [
    "id",
    "name",
    # "slug",
    "introduction",
    "conclusion",
    "questions",
    "tags",
    "difficulty_average",
    "language",
    "author",
    "image_background_url",
    "has_audio",
    # "publish", "spotlight",
    # "relationships",
    "question_count",
    "questions_categories_list",
    "questions_tags_list",
    "questions_authors_list",
    "created",
    "updated",
]


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = QUIZ_FIELDS


class QuizWithQuestionOrderSerializer(serializers.ModelSerializer):
    questions = QuizQuestionSerializer(source="quizquestion_set", many=True)

    class Meta:
        model = Quiz
        fields = QUIZ_FIELDS


class QuizFullSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Quiz
        fields = QUIZ_FIELDS
