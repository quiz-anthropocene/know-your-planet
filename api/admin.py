import csv
import json
from datetime import datetime

# from io import StringIO

from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.utils.html import mark_safe

# from django.core.management import call_command

from api.models import (
    Question,
    Category,
    Tag,
    Quiz,
    QuestionStat,
    QuizStat,
    Contribution,
)


class ExportMixin:
    """
    Add export actions
    https://books.agiliq.com/projects/django-admin-cookbook/en/latest/export.html
    """

    def export_as_csv(self, request, queryset):
        """
        TODO: improve ManyToMany management (currently: hack to add tags to Question)
        """
        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={self.model._meta} - {datetime.now().date()}.csv"

        # field_names = [field.name for field in self.model._meta.get_fields()]
        field_names = [field.name for field in self.model._meta.fields]

        writer = csv.writer(response)

        if queryset.model.__name__ == "Question":
            writer.writerow(field_names + ["tags"])
        else:
            writer.writerow(field_names)

        for obj in queryset:
            if queryset.model.__name__ == "Question":
                writer.writerow(
                    [getattr(obj, field) for field in field_names]
                    + [obj.tags_list_string]
                )
            else:
                writer.writerow([getattr(obj, field) for field in field_names])

        return response

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={self.model._meta} - {datetime.now().date()}.json"

        response.write(
            serializers.serialize("json", list(queryset), ensure_ascii=False)
        )

        return response

    def export_as_yaml(self, request, queryset):
        """
        TODO: escape " (\")
        """
        response = HttpResponse(content_type="text/yaml")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={self.model._meta} - {datetime.now().date()}.yaml"

        response.write(
            serializers.serialize("yaml", queryset)
            .encode()
            .decode("unicode_escape")
            .encode("utf-8")
        )

        return response

    def export_all_question_as_yaml(self, request, queryset):
        return self.export_as_yaml(request, Question.objects.all().order_by("pk"))

    def export_all_questioncategory_as_yaml(self, request, queryset):
        return self.export_as_yaml(request, Category.objects.all().order_by("pk"))

    def export_all_questiontag_as_yaml(self, request, queryset):
        return self.export_as_yaml(request, Tag.objects.all().order_by("pk"))

    def export_all_questionstat_as_yaml(self, request, queryset):
        return self.export_as_yaml(request, QuestionStat.objects.all().order_by("pk"))

    # def export_all_as_yaml(self, request):
    #     meta = self.model._meta

    #     response = HttpResponse(content_type='text/yaml')
    #     response['Content-Disposition'] = 'attachment; filename={}.yaml'.format(meta)

    #     out = StringIO()
    #     call_command('dumpdata', 'api.question', '--format=yaml', '--pretty', stdout=out)

    #     response.write(out.getvalue())

    #     return response

    export_as_csv.short_description = "Export Selected (CSV)"
    export_as_json.short_description = "Export Selected (JSON)"
    export_as_yaml.short_description = "Export Selected (YAML)"
    export_all_question_as_yaml.short_description = "Export All (YAML)"
    export_all_questioncategory_as_yaml.short_description = "Export All (YAML)"
    export_all_questiontag_as_yaml.short_description = "Export All (YAML)"
    export_all_questionstat_as_yaml.short_description = "Export All (YAML)"


class QuestionAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "text",
        "type",
        "category",
        "tags_list_string",
        "difficulty",
        "author",
        "publish",
        # "validation_status",
        "has_answer_explanation",
        "has_answer_additional_link",
        "has_answer_image_link",
        "answer_count",
        "answer_success_count",
        "answer_success_rate",
    )
    list_filter = (
        "type",
        "category",
        "tags",
        "difficulty",
        "author",
        "publish",
        "validation_status",
    )
    ordering = ("id",)  # "answer_count", "answer_success_rate",
    actions = [
        "export_as_csv",
        "export_as_json",
        "export_as_yaml",
        "export_all_question_as_yaml",
    ]
    filter_horizontal = ("tags",)
    readonly_fields = (
        "show_answer_image",
        "answer_count",
        "answer_success_count",
        "answer_success_rate",
    )

    def has_answer_explanation(self, instance):
        return instance.has_answer_explanation

    has_answer_explanation.short_description = "Explication"
    has_answer_explanation.boolean = True

    def has_answer_additional_link(self, instance):
        return instance.has_answer_additional_link

    has_answer_additional_link.short_description = "Lien(s)"
    has_answer_additional_link.boolean = True

    def has_answer_image_link(self, instance):
        return instance.has_answer_image_link

    has_answer_image_link.short_description = "Image"
    has_answer_image_link.boolean = True

    def show_answer_image(self, instance):
        if instance.answer_image_link:
            return mark_safe(
                f'<a href="{instance.answer_image_link}" target="_blank">'
                f'<img src="{instance.answer_image_link}" height=300 />'
                f"</a>"
            )
        else:
            return mark_safe("<div>champ 'Answer image link' vide</div>")

    show_answer_image.short_description = (
        "L'image du champ 'Answer image link' (cliquer pour agrandir)"
    )
    show_answer_image.allow_tags = True


class CategoryAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "name",
        "name_long",
        "question_count",
    )
    ordering = ("id",)
    actions = [
        "export_as_csv",
        "export_as_json",
        "export_as_yaml",
        "export_all_questioncategory_as_yaml",
    ]


class TagAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "name",
        "question_count",
    )
    ordering = ("name",)
    actions = [
        "export_as_csv",
        "export_as_json",
        "export_as_yaml",
        "export_all_questiontag_as_yaml",
    ]


class QuizAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "name",
        "question_count",
        "author",
        "categories_list",
        "tags_list",
        "difficulty_average",
        "publish",
        "answer_count",
    )
    list_filter = ("publish",)
    ordering = ("id",)
    filter_horizontal = ("questions",)
    readonly_fields = ("answer_count",)
    actions = ["export_as_csv", "export_as_json", "export_as_yaml"]


class QuestionStatAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "question",
        "answer_choice",
        "source",
        "created",
    )
    list_filter = ("source",)
    ordering = ("id",)
    actions = [
        "export_as_csv",
        "export_as_json",
        "export_as_yaml",
        "export_all_questionstat_as_yaml",
    ]

    def changelist_view(self, request, extra_context=None):
        """
        show chart of answers per day
        https://dev.to/danihodovic/integrating-chart-js-with-django-admin-1kjb

        Corresponding template in templates/admin/api/questionstat/change_list.html
        """
        # Aggregate answers per day
        if settings.DEBUG:  # sqlite
            chart_data_query = QuestionStat.objects.extra(
                select={"day": "date(created)"}
            )
        else:  # postgresql
            chart_data_query = QuestionStat.objects.extra(
                select={"day": "to_char(created, 'YYYY-MM-DD')"}
            )
        chart_data_query = (
            chart_data_query.values("day").annotate(y=Count("created")).order_by("-day")
        )

        # get answers since today
        if chart_data_query[0]["day"] != str(datetime.now().date()):
            chart_data_list = [{"day": str(datetime.now().date()), "y": 0}] + list(
                chart_data_query
            )
        else:
            chart_data_list = list(chart_data_query)

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(chart_data_list, cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


class QuizStatAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "quiz",
        "question_count",
        "answer_success_count",
        "created",
    )
    list_filter = ("quiz",)
    ordering = ("id",)
    actions = ["export_as_csv", "export_as_json", "export_as_yaml"]

    def changelist_view(self, request, extra_context=None):
        """
        show chart of answers per day
        https://dev.to/danihodovic/integrating-chart-js-with-django-admin-1kjb

        Corresponding template in templates/admin/api/quizstat/change_list.html
        """
        # Aggregate answers per day
        if settings.DEBUG:  # sqlite
            chart_data_query = QuizStat.objects.extra(select={"day": "date(created)"})
        else:  # postgresql
            chart_data_query = QuizStat.objects.extra(
                select={"day": "to_char(created, 'YYYY-MM-DD')"}
            )
        chart_data_query = (
            chart_data_query.values("day").annotate(y=Count("created")).order_by("-day")
        )

        # get answers since today
        if chart_data_query[0]["day"] != str(datetime.now().date()):
            chart_data_list = [{"day": str(datetime.now().date()), "y": 0}] + list(
                chart_data_query
            )
        else:
            chart_data_list = list(chart_data_query)

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(chart_data_list, cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


class ContributionAdmin(admin.ModelAdmin, ExportMixin):
    list_display = (
        "id",
        "is_question",
        "text",
        "created",
    )
    readonly_fields = (
        "text",
        "description",
    )

    def has_add_permission(self, request, obj=None):
        return False

    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False


class LogEntryAdmin(admin.ModelAdmin):
    """
    https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#logentry-objects
    """

    list_display = (
        "object_repr",
        "content_type",
        "action_flag",
        "user",
        "action_time",
    )
    list_filter = (
        "content_type",
        "user",
    )
    ordering = ("-action_time",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuestionStat, QuestionStatAdmin)
admin.site.register(QuizStat, QuizStatAdmin)
admin.site.register(Contribution, ContributionAdmin)
admin.site.register(admin.models.LogEntry, LogEntryAdmin)
