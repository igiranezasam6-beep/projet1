from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm


urlpatterns = [
    path("", views.home, name="home"),
    path("signup/eleve/", views.signup_student, name="signup_student"),
    path("signup/enseignant/", views.signup_teacher, name="signup_teacher"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("exercices/", views.exercise_list, name="exercise_list"),
    path("exercices/nouveau/", views.exercise_create, name="exercise_create"),
    path("exercices/<int:exercise_id>/", views.exercise_detail, name="exercise_detail"),
    path("forum/", views.forum_list, name="forum_list"),
    path("forum/nouveau/", views.forum_topic_create, name="forum_topic_create"),
    path("forum/<int:topic_id>/", views.forum_topic_detail, name="forum_topic_detail"),
    path("chatbot/", views.chatbot, name="chatbot"),
]

