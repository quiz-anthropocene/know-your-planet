from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django_tables2.views import SingleTableView

from questions.models import Question
from questions.tables import QuestionTable
from quizs.models import Quiz
from quizs.tables import QuizTable
from users.models import User


class ProfileInfoView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile/info.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user


class ProfileQuestionsView(LoginRequiredMixin, SingleTableView):
    model = Question
    template_name = "profile/questions.html"
    context_object_name = "user_questions"
    table_class = QuestionTable

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("category", "author_link", "validator_link").prefetch_related("tags")
        qs = qs.filter(author_link=self.request.user)
        qs = qs.order_by("-created")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ProfileQuizsView(LoginRequiredMixin, SingleTableView):
    model = Quiz
    template_name = "profile/quizs.html"
    context_object_name = "user_quizs"
    table_class = QuizTable

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("author_link").prefetch_related("tags")
        qs = qs.filter(author_link=self.request.user)
        qs = qs.order_by("-created")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context