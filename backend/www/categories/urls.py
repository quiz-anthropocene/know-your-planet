from django.urls import include, path
from django.views.generic.base import RedirectView

from www.categories.views import CategoryDetailQuestionsView, CategoryDetailView, CategoryListView


app_name = "categories"

urlpatterns = [
    path("", CategoryListView.as_view(), name="list"),
    # path("<int:pk>/", CategoryDetailView.as_view(), name="detail"),
    path(
        "<int:pk>/",
        include(
            [
                # path("", CategoryDetailView.as_view(), name="detail"),
                path(
                    "",
                    RedirectView.as_view(pattern_name="categories:detail_view", permanent=False),
                    name="detail",
                ),
                path("view/", CategoryDetailView.as_view(), name="detail_view"),
                path("questions/", CategoryDetailQuestionsView.as_view(), name="detail_questions"),
            ]
        ),
    ),
]
