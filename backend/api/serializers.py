from rest_framework import serializers

from api.categories.serializers import CategorySerializer, CategoryStringSerializer
from api.models import Question, Quiz, QuizQuestion
from api.tags.serializers import TagSerializer, TagStringSerializer


class SimpleChoiceSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


"""
QUESTION DIFFICULTY
"""


class QuestionDifficultyChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


"""
QUESTION
"""

QUESTION_FIELDS = [
    "id",
    "text",
    "hint",
    "type",
    "difficulty",
    "language",
    "author",
    "category",
    "tags",
    "answer_option_a",
    "answer_option_b",
    "answer_option_c",
    "answer_option_d",
    "has_ordered_answers",
    "answer_correct",
    "answer_explanation",
    "answer_audio",
    "answer_video",
    "answer_accessible_url",
    "answer_accessible_url_text",
    "answer_scientific_url",
    "answer_scientific_url_text",
    "answer_reading_recommendation",
    "answer_image_url",
    "answer_image_explanation",
    "answer_count_agg",
    "answer_success_count_agg",
    "added",
    "created",
    "updated",
]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = QUESTION_FIELDS


class QuestionFullStringSerializer(serializers.ModelSerializer):
    category = CategoryStringSerializer()
    tags = TagStringSerializer(many=True)

    class Meta:
        model = Question
        fields = QUESTION_FIELDS


class QuestionFullObjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Question
        fields = QUESTION_FIELDS


"""
QUIZ QUESTION
"""


class QuizQuestionSerializer(serializers.ModelSerializer):
    # override QuizQuestion id with question_id
    id = serializers.ReadOnlyField(source="question.id")

    class Meta:
        model = QuizQuestion
        fields = ["id", "order"]


"""
QUIZ
"""

QUIZ_FIELDS = [
    "id",
    "name",
    "introduction",
    "conclusion",
    "language",
    "author",
    "image_background_url",
    "questions",
    "tags",
    "question_count",
    "questions_categories_list",
    "questions_tags_list",
    "questions_authors_list",
    "difficulty_average",
    "created",
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
