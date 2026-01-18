from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('create/', views.create_discussion, name='create_discussion'),
    path('<int:pk>/', views.discussion_detail, name='discussion_detail'),
]
