from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chatbot'),
    path('api/response/', views.get_response, name='chatbot_response'),
]
