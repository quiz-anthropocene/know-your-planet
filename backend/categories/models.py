from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, help_text="Le nom de la catégorie")
    name_long = models.CharField(max_length=150, blank=False, help_text="Le nom allongé de la catégorie")
    description = RichTextField(blank=True, help_text="Une description de la catégorie")
    created = models.DateField(auto_now_add=True, help_text="La date de création de la catégorie")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["pk"]
        constraints = [models.UniqueConstraint(fields=["name"], name="category_name_unique")]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={"pk": self.id})

    @property
    def question_count(self) -> int:
        return self.questions.count()

    @property
    def question_validated_count(self) -> int:
        return self.questions.validated().count()

    # Admin
    question_validated_count.fget.short_description = "Questions (validées)"
