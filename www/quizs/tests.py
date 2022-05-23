from django.test import TestCase
from django.urls import reverse

from core import constants
from quizs.factories import QuizFactory
from quizs.models import Quiz
from users import constants as user_constants
from users.factories import DEFAULT_PASSWORD, UserFactory


QUIZ_DETAIL_URLS = [
    "quizs:detail_view",
    "quizs:detail_edit",
    "quizs:detail_questions",
    "quizs:detail_contributions",
    "quizs:detail_stats",
    "quizs:detail_history",
]

QUIZ_CREATE_FORM_DEFAULT = {
    "name": "Quiz 1",
    "language": constants.LANGUAGE_FRENCH,
    "visibility": constants.VISIBILITY_PUBLIC,
}


class QuizListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(roles=[])
        cls.user_contributor = UserFactory()
        cls.quiz_1 = QuizFactory(name="Quiz 1")
        cls.quiz_2 = QuizFactory(name="Quiz 2")

    def test_anonymous_user_cannot_access_quiz_list(self):
        url = reverse("quizs:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/quizs/")

    def test_only_contributor_can_access_quiz_list(self):
        self.client.login(email=self.user.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        self.client.login(email=self.user_contributor.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["quizs"]), 2)


class QuizDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.quiz_1 = QuizFactory(name="Quiz 1")
        cls.quiz_2 = QuizFactory(name="Quiz 2")

    def test_anonymous_user_cannot_access_quiz_detail(self):
        for edit_url in QUIZ_DETAIL_URLS:
            url = reverse(edit_url, args=[self.quiz_1.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith("/accounts/login/"))

    def test_contributor_can_access_quiz_detail(self):
        self.client.login(email=self.user.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:detail_view", args=[self.quiz_1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["quiz"].id, self.quiz_1.id)


class QuizDetailEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_contributor_1 = UserFactory()
        cls.user_contributor_2 = UserFactory()
        cls.user_admin = UserFactory(roles=[user_constants.USER_ROLE_ADMINISTRATOR])
        cls.quiz_1 = QuizFactory(name="Quiz 1", author=cls.user_contributor_1, visibility=constants.VISIBILITY_PUBLIC)
        cls.quiz_2 = QuizFactory(name="Quiz 2", author=cls.user_contributor_1, visibility=constants.VISIBILITY_PRIVATE)

    def test_author_or_admin_can_edit_public_quiz(self):
        for user in [self.user_contributor_1, self.user_admin]:
            self.client.login(email=user.email, password=DEFAULT_PASSWORD)
            url = reverse("quizs:detail_edit", args=[self.quiz_1.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, '<form id="quiz_edit_form" ')
        # other contributors can't edit
        self.client.login(email=self.user_contributor_2.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:detail_edit", args=[self.quiz_1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '<form id="quiz_edit_form" ')
        self.assertContains(response, "Vous n'avez pas les droits nécessaires")

    def test_only_author_can_edit_private_quiz(self):
        # author can edit
        self.client.login(email=self.user_contributor_1.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:detail_edit", args=[self.quiz_2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form id="quiz_edit_form" ')
        # other contributors can't edit
        for user in [self.user_contributor_2, self.user_admin]:
            self.client.login(email=user.email, password=DEFAULT_PASSWORD)
            url = reverse("quizs:detail_edit", args=[self.quiz_2.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertNotContains(response, '<form id="quiz_edit_form" ')
            self.assertContains(response, "Vous n'avez pas les droits nécessaires")


class QuizDetailQuestionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_contributor_1 = UserFactory()
        cls.user_contributor_2 = UserFactory()
        cls.user_admin = UserFactory(roles=[user_constants.USER_ROLE_ADMINISTRATOR])
        cls.quiz_1 = QuizFactory(name="Quiz 1", author=cls.user_contributor_1)

    def test_author_or_admin_can_edit_quiz_question_list(self):
        for user in [self.user_contributor_1, self.user_admin]:
            self.client.login(email=user.email, password=DEFAULT_PASSWORD)
            url = reverse("quizs:detail_questions", args=[self.quiz_1.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Modifier les questions")
            self.assertContains(response, '<form id="quiz_question_edit_form" ')
        # other contributors can't edit
        self.client.login(email=self.user_contributor_2.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:detail_questions", args=[self.quiz_1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Modifier les questions")
        self.assertNotContains(response, '<form id="quiz_question_edit_form" ')


class QuizCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(roles=[])
        cls.user_contributor = UserFactory()

    def test_anonymous_user_cannot_access_quiz_create(self):
        url = reverse("quizs:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/accounts/login/"))

    def test_only_contributor_can_access_quiz_create(self):
        self.client.login(email=self.user.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        self.client.login(email=self.user_contributor.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contributor_can_create_quiz(self):
        self.client.login(email=self.user_contributor.email, password=DEFAULT_PASSWORD)
        url = reverse("quizs:create")
        response = self.client.post(url, data=QUIZ_CREATE_FORM_DEFAULT)
        self.assertEqual(response.status_code, 302)  # 201
        self.assertEqual(Quiz.objects.count(), 1)