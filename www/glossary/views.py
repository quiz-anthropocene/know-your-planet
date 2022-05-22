from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, DetailView, UpdateView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from api.glossary.serializers import GlossaryItemSerializer
from core.mixins import ContributorUserRequiredMixin
from glossary.forms import GlossaryItemCreateForm, GlossaryItemEditForm
from glossary.models import GlossaryItem
from glossary.tables import GlossaryTable


class GlossaryListView(ContributorUserRequiredMixin, SingleTableMixin, FilterView):
    model = GlossaryItem
    template_name = "glossary/list.html"
    context_object_name = "glossary"
    table_class = GlossaryTable


class GlossaryItemDetailView(ContributorUserRequiredMixin, DetailView):
    model = GlossaryItem
    template_name = "glossary/detail_view.html"
    context_object_name = "glossary_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        glossary_item = self.get_object()
        context["glossary_item_dict"] = GlossaryItemSerializer(glossary_item).data
        return context


class GlossaryItemDetailEditView(ContributorUserRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = GlossaryItemEditForm
    template_name = "glossary/detail_edit.html"
    context_object_name = "glossary_item"
    success_message = "Le terme a été mis à jour."
    # success_url = reverse_lazy("glossary:detail_view")

    def get_object(self):
        return get_object_or_404(GlossaryItem, id=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse_lazy("glossary:detail_view", args=[self.kwargs.get("pk")])


class GlossaryItemCreateView(ContributorUserRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GlossaryItemCreateForm
    template_name = "glossary/create.html"
    success_url = reverse_lazy("glossary:list")
    # success_message = ""

    def get_success_message(self, cleaned_data):
        return mark_safe(f"Le terme <strong>{self.object.name}</strong> a été crée avec succès.")
