from datetime import date, timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone

from core import constants
from questions.models import Question
from quizs.models import Quiz


class ContributionQuerySet(models.QuerySet):
    def exclude_contributor_comments(self):
        return self.exclude(type=constants.CONTRIBUTION_TYPE_COMMENT_CONTRIBUTOR)

    def exclude_replies(self):
        return self.exclude(type=constants.CONTRIBUTION_TYPE_REPLY)

    def exclude_contributor_work(self):
        return self.exclude_contributor_comments().exclude_replies()

    def only_replies(self):
        return self.filter(type=constants.CONTRIBUTION_TYPE_REPLY)

    def exclude_errors(self):
        return self.exclude(type=constants.CONTRIBUTION_TYPE_ERROR_APP)

    def last_30_days(self):
        return self.filter(created__date__gte=(date.today() - timedelta(days=30)))


class Contribution(models.Model):
    CONTRIBUTION_CHOICE_FIELDS = ["type", "status"]
    CONTRIBUTION_FK_FIELDS = ["question", "quiz", "author"]
    CONTRIBUTION_READONLY_FIELDS = ["parent", "created", "updated"]
    text = models.TextField(
        verbose_name="Texte",
        blank=False,
        help_text="Une question, un commentaire…",
    )
    description = models.TextField(verbose_name="Information supplémentaire", blank=True)
    type = models.CharField(
        verbose_name="Type", max_length=150, choices=constants.CONTRIBUTION_TYPE_CHOICES, blank=True
    )

    question = models.ForeignKey(
        verbose_name="Question",
        to=Question,
        related_name="contributions",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    quiz = models.ForeignKey(
        verbose_name="Quiz", to=Quiz, related_name="contributions", on_delete=models.CASCADE, null=True, blank=True
    )
    author = models.ForeignKey(
        verbose_name="Auteur",
        to=settings.AUTH_USER_MODEL,
        related_name="contributions",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    status = models.CharField(
        verbose_name="Statut",
        max_length=150,
        choices=constants.CONTRIBUTION_STATUS_CHOICES,
        # default=constants.CONTRIBUTION_STATUS_PENDING,
        blank=True,
    )

    parent = models.ForeignKey(
        verbose_name="En réponse à", to="self", related_name="replies", on_delete=models.CASCADE, null=True, blank=True
    )

    created = models.DateTimeField(verbose_name="Date de création", default=timezone.now)
    updated = models.DateTimeField(verbose_name="Date de dernière modification", auto_now=True)

    objects = ContributionQuerySet.as_manager()

    def __str__(self):
        return f"{self.text}"

    @property
    def get_author(self) -> str:
        return self.author or "Utilisateur anonyme"

    def get_reply_type(self) -> str:
        return self.get_type_display().replace(" contributeur", "")

    @property
    def has_replies(self) -> bool:
        return self.replies.exists()

    @property
    def has_replies_reply(self) -> bool:
        return self.replies.only_replies().exists()

    @property
    def processed(self) -> str:
        if self.status == constants.CONTRIBUTION_STATUS_NEW:
            return "❌"
        if self.status == constants.CONTRIBUTION_STATUS_PENDING:
            return "📝"
        return "✅"
