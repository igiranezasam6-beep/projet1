from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    ChatbotForm,
    ExerciseCommentForm,
    ExerciseForm,
    ForumPostForm,
    ForumTopicForm,
    StudentSignUpForm,
    TeacherSignUpForm,
)
from .models import Exercise, ForumTopic, Profile


def home(request: HttpRequest) -> HttpResponse:
    latest_exercises = Exercise.objects.all()[:6]
    return render(request, "learning/home.html", {"latest_exercises": latest_exercises})


def signup_student(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte élève créé.")
            return redirect("home")
    else:
        form = StudentSignUpForm()
    return render(
        request,
        "learning/signup.html",
        {"form": form, "title": "Créer un compte élève", "subtitle": "Accès immédiat aux exercices."},
    )


def signup_teacher(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "Compte enseignant créé. En attente de vérification par un administrateur.")
            return redirect("home")
    else:
        form = TeacherSignUpForm()
    return render(
        request,
        "learning/signup.html",
        {"form": form, "title": "Créer un compte enseignant", "subtitle": "Le compte doit être vérifié avant dépôt."},
    )


def _is_verified_teacher(request: HttpRequest) -> bool:
    if not request.user.is_authenticated:
        return False
    profile = getattr(request.user, "profile", None)
    return bool(profile and profile.role == Profile.Role.TEACHER and profile.is_verified)


def exercise_list(request: HttpRequest) -> HttpResponse:
    qs = Exercise.objects.all()
    subject = (request.GET.get("subject") or "").strip()
    school_level = (request.GET.get("level") or "").strip()
    theme = (request.GET.get("theme") or "").strip()
    q = (request.GET.get("q") or "").strip()

    if subject:
        qs = qs.filter(subject__icontains=subject)
    if school_level:
        qs = qs.filter(school_level__icontains=school_level)
    if theme:
        qs = qs.filter(theme__icontains=theme)
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))

    return render(
        request,
        "learning/exercise_list.html",
        {
            "exercises": qs[:200],
            "filters": {"subject": subject, "level": school_level, "theme": theme, "q": q},
            "can_upload": _is_verified_teacher(request),
        },
    )


def exercise_detail(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    session_key = f"viewed_exercise_{exercise_id}"
    if not request.session.get(session_key):
        Exercise.objects.filter(pk=exercise_id).update(view_count=exercise.view_count + 1)
        request.session[session_key] = True
        exercise.refresh_from_db(fields=["view_count"])

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Connectez-vous pour poser une question.")
            return redirect("login")
        comment_form = ExerciseCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.exercise = exercise
            comment.author = request.user
            comment.save()
            messages.success(request, "Question publiée.")
            return redirect("exercise_detail", exercise_id=exercise_id)
    else:
        comment_form = ExerciseCommentForm()

    return render(
        request,
        "learning/exercise_detail.html",
        {"exercise": exercise, "comment_form": comment_form},
    )


@login_required
def exercise_create(request: HttpRequest) -> HttpResponse:
    if not _is_verified_teacher(request):
        messages.error(request, "Accès réservé aux enseignants vérifiés.")
        return redirect("exercise_list")

    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.created_by = request.user
            exercise.save()
            messages.success(request, "Exercice publié.")
            return redirect("exercise_detail", exercise_id=exercise.id)
    else:
        form = ExerciseForm()
    return render(request, "learning/exercise_form.html", {"form": form})


def forum_list(request: HttpRequest) -> HttpResponse:
    topics = ForumTopic.objects.all()[:200]
    return render(request, "learning/forum_list.html", {"topics": topics})


@login_required
def forum_topic_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ForumTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            messages.success(request, "Sujet créé.")
            return redirect("forum_topic_detail", topic_id=topic.id)
    else:
        form = ForumTopicForm()
    return render(request, "learning/forum_topic_form.html", {"form": form})


def forum_topic_detail(request: HttpRequest, topic_id: int) -> HttpResponse:
    topic = get_object_or_404(ForumTopic, pk=topic_id)

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Connectez-vous pour répondre.")
            return redirect("login")
        post_form = ForumPostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            messages.success(request, "Réponse publiée.")
            return redirect("forum_topic_detail", topic_id=topic_id)
    else:
        post_form = ForumPostForm()

    return render(request, "learning/forum_topic_detail.html", {"topic": topic, "post_form": post_form})


def chatbot(request: HttpRequest) -> HttpResponse:
    answer = None
    suggestions = []

    if request.method == "POST":
        form = ChatbotForm(request.POST)
        if form.is_valid():
            level = (form.cleaned_data.get("school_level") or "").strip()
            question = (form.cleaned_data.get("question") or "").strip().lower()

            faq = [
                (["créer", "compte", "inscription"], "Allez dans « Créer un compte » (élève ou enseignant)."),
                (["exercice", "télécharger", "download"], "Ouvrez un exercice puis utilisez le bouton « Télécharger »."),
                (["corrigé", "solution"], "Le corrigé est visible sur la page de l’exercice (texte ou fichier)."),
                (["enseignant", "vérifié", "verification"], "Les comptes enseignants sont vérifiés via l’administrateur."),
                (["forum", "discussion"], "Utilisez l’onglet « Forum » pour créer un sujet ou répondre."),
            ]

            answer = "Je n’ai pas trouvé de réponse exacte. Essayez avec des mots-clés (ex: inscription, corrigé, forum)."
            for keywords, text in faq:
                if any(k in question for k in keywords):
                    answer = text
                    break

            if level:
                suggestions = list(
                    Exercise.objects.filter(school_level__icontains=level).values_list("id", "title")[:5]
                )

    else:
        form = ChatbotForm()

    return render(
        request,
        "learning/chatbot.html",
        {"form": form, "answer": answer, "suggestions": suggestions},
    )
