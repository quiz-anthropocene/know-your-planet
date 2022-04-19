from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django_tables2.views import SingleTableView

from api.categories.serializers import CategorySerializer
from categories.forms import CategoryEditForm
from categories.models import Category
from categories.tables import CategoryTable
from questions.models import Question


class CategoryListView(LoginRequiredMixin, SingleTableView):
    model = Category
    template_name = "categories/list.html"
    context_object_name = "categories"
    table_class = CategoryTable


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "categories/detail_view.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context["category_dict"] = CategorySerializer(category).data
        return context


class CategoryDetailEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CategoryEditForm
    template_name = "categories/detail_edit.html"
    success_message = "La catégorie a été mise à jour."
    # success_url = reverse_lazy("categories:detail_view")

    def get_object(self):
        return get_object_or_404(Category, id=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse_lazy("categories:detail_view", args=[self.kwargs.get("pk")])


class CategoryDetailQuestionsView(LoginRequiredMixin, SingleTableView):
    model = Question
    template_name = "categories/detail_questions.html"
    context_object_name = "questions"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.prefetch_related("tags")
        qs = qs.filter(category_id=self.kwargs.get("pk"))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(id=self.kwargs.get("pk"))
        return context
