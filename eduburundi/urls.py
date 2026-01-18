from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('resources/', include('resources.urls')),
    path('forum/', include('forum.urls')),
    path('chatbot/', include('chatbot.urls')),
]
