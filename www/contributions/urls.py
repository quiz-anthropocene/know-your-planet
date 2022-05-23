from django.urls import include, path
from django.views.generic.base import RedirectView

from www.contributions.views import (
    ContributionDetailEditView,
    ContributionDetailReplyCreateView,
    ContributionDetailView,
    ContributionListView,
)


app_name = "contributions"

urlpatterns = [
    path("", ContributionListView.as_view(), name="list"),
    path(
        "<int:pk>/",
        include(
            [
                # path("", ContributionDetailView.as_view(), name="detail"),
                path(
                    "",
                    RedirectView.as_view(pattern_name="contributions:detail_view", permanent=False),
                    name="detail",
                ),
                path("view/", ContributionDetailView.as_view(), name="detail_view"),
                path("edit/", ContributionDetailEditView.as_view(), name="detail_edit"),
                path("reply/", ContributionDetailReplyCreateView.as_view(), name="detail_reply_create"),
            ]
        ),
    ),
]