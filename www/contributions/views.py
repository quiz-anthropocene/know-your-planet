from django.views.generic import DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from api.contributions.serializers import ContributionSerializer
from contributions.filters import ContributionFilter
from contributions.models import Contribution
from contributions.tables import ContributionTable
from core.mixins import ContributorUserRequiredMixin


class ContributionListView(ContributorUserRequiredMixin, SingleTableMixin, FilterView):
    model = Contribution
    template_name = "contributions/list.html"
    context_object_name = "contributions"
    table_class = ContributionTable
    filterset_class = ContributionFilter

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.exclude_errors().exclude_answers().order_by("-created")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_params = [value for (key, value) in self.request.GET.items() if ((key not in ["page"]) and value)]
        if len(request_params):
            context["active_filters"] = True
        return context


class ContributionDetailView(ContributorUserRequiredMixin, DetailView):
    model = Contribution
    template_name = "contributions/detail_view.html"
    context_object_name = "contribution"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contribution = self.get_object()
        context["contribution_dict"] = ContributionSerializer(contribution).data
        return context
