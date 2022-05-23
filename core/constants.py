QUESTION_TYPE_QCM = "QCM"
QUESTION_TYPE_QCM_RM = "QCM-RM"
QUESTION_TYPE_VF = "VF"
QUESTION_TYPE_CHOICES = [
    (QUESTION_TYPE_QCM, "Questionnaire à choix multiples"),
    (QUESTION_TYPE_QCM_RM, "Questionnaire à choix multiples avec réponses multiples"),
    (QUESTION_TYPE_VF, "Vrai ou Faux"),
]
QUESTION_TYPE_CHOICE_LIST = [c[0] for c in QUESTION_TYPE_CHOICES]

QUESTION_TYPE_VF_CHOICE_LIST = ["a", "b"]
QUESTION_TYPE_QCM_CHOICE_LIST = ["a", "b", "c", "d"]

QUESTION_VALIDATION_STATUS_NEW = "Brouillon"
QUESTION_VALIDATION_STATUS_IN_PROGRESS = "A valider"
QUESTION_VALIDATION_STATUS_OK = "Validée"
QUESTION_VALIDATION_STATUS_ASIDE = "Écartée temporairement"
QUESTION_VALIDATION_STATUS_REMOVED = "Écartée"
QUESTION_VALIDATION_STATUS_CHOICE_LIST = [
    QUESTION_VALIDATION_STATUS_NEW,
    QUESTION_VALIDATION_STATUS_IN_PROGRESS,
    QUESTION_VALIDATION_STATUS_OK,
    QUESTION_VALIDATION_STATUS_ASIDE,
    QUESTION_VALIDATION_STATUS_REMOVED,
]
QUESTION_VALIDATION_STATUS_CHOICES = [(vs, vs) for vs in QUESTION_VALIDATION_STATUS_CHOICE_LIST]

QUESTION_DIFFICULTY_EASY = 1
QUESTION_DIFFICULTY_HARD = 3
QUESTION_DIFFICULTY_OPTIONS = [
    (0, "Junior", "🧸"),
    (QUESTION_DIFFICULTY_EASY, "Facile", "🏆"),
    (2, "Moyen", "🏆🏆"),
    (QUESTION_DIFFICULTY_HARD, "Difficile", "🏆🏆🏆"),
    (4, "Expert", "🏆🏆🏆🏆"),
]
QUESTION_DIFFICULTY_CHOICES = [(c[0], c[1]) for c in QUESTION_DIFFICULTY_OPTIONS]
QUESTION_DIFFICULTY_CHOICE_LIST = [c[0] for c in QUESTION_DIFFICULTY_OPTIONS]

QUESTION_ANSWER_CHOICE_LIST = [
    "a",
    "b",
    "c",
    "d",
    "ab",
    "ac",
    "ad",
    "bc",
    "bd",
    "cd",
    "abc",
    "abd",
    "acd",
    "bcd",
    "abcd",
]
QUESTION_ANSWER_CHOICES = [(a, a) for a in QUESTION_ANSWER_CHOICE_LIST]

QUIZ_RELATIONSHIP_CHOICE_LIST = [
    "suivant",
    # "précédent",
    "jumeau",
    "similaire",
    "traduction",
]

CONTRIBUTION_TYPE_NEW_QUESTION = "NEW_QUESTION"
CONTRIBUTION_TYPE_NEW_QUIZ = "NEW_QUIZ"
CONTRIBUTION_TYPE_COMMENT_APP = "COMMENT_APP"
CONTRIBUTION_TYPE_COMMENT_QUESTION = "COMMENT_QUESTION"
CONTRIBUTION_TYPE_COMMENT_QUIZ = "COMMENT_QUIZ"
CONTRIBUTION_TYPE_REPLY = "REPLY"
CONTRIBUTION_TYPE_ERROR_APP = "ERROR_APP"
CONTRIBUTION_TYPE_CHOICES = [
    (CONTRIBUTION_TYPE_NEW_QUESTION, "Nouvelle question"),
    (CONTRIBUTION_TYPE_NEW_QUIZ, "Nouveau quiz"),
    (CONTRIBUTION_TYPE_COMMENT_APP, "Commentaire application"),
    (CONTRIBUTION_TYPE_COMMENT_QUESTION, "Commentaire question"),
    (CONTRIBUTION_TYPE_COMMENT_QUIZ, "Commentaire quiz"),
    (CONTRIBUTION_TYPE_REPLY, "Réponse"),
    (CONTRIBUTION_TYPE_ERROR_APP, "Erreur application"),
]

CONTRIBUTION_STATUS_PENDING = "PENDING"
CONTRIBUTION_STATUS_PROCESSED = "PROCESSED"
CONTRIBUTION_STATUS_REPLIED = "REPLIED"
CONTRIBUTION_STATUS_IGNORED = "IGNORED"
CONTRIBUTION_STATUS_CHOICES = [
    (CONTRIBUTION_STATUS_PENDING, "À traiter"),
    (CONTRIBUTION_STATUS_PROCESSED, "Traité"),
    (CONTRIBUTION_STATUS_REPLIED, "Répondu"),
    (CONTRIBUTION_STATUS_IGNORED, "Ignoré"),
]

LANGUAGE_FRENCH = "Français"
LANGUAGE_ENGLISH = "English"
LANGUAGE_CHOICE_LIST = [
    LANGUAGE_FRENCH,
    LANGUAGE_ENGLISH,
]
LANGUAGE_CHOICES = [(lang, lang) for lang in LANGUAGE_CHOICE_LIST]

NOTION_QUESTIONS_IMPORT_SCOPE_CHOICES = [
    (0, "100 dernières questions modifiées"),
    # below are currently hidden
    (1, "1 à 200"),
    (2, "200 à 400"),
    (3, "400 à 600"),
    (4, "600 à 800"),
    (5, "800 et plus"),
]
NOTION_QUESTIONS_IMPORT_SCOPE_LIST = [value for (value, label) in NOTION_QUESTIONS_IMPORT_SCOPE_CHOICES]

VISIBILITY_PUBLIC = "PUBLIC"
VISIBILITY_HIDDEN = "HIDDEN"
VISIBILITY_PRIVATE = "PRIVATE"
VISIBILITY_CHOICES = (
    (VISIBILITY_PUBLIC, "Publique (dans l'export et dans l'application)"),
    (VISIBILITY_HIDDEN, "Caché (dans l'export mais pas visible dans l'application)"),
    (VISIBILITY_PRIVATE, "Privé (pas dans l'export ni dans l'application)"),
)

BOOLEAN_CHOICES = [(True, "Vrai"), (False, "Faux")]

EMPTY_CHOICE = (("", ""),)