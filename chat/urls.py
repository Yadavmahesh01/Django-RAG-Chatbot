
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_window, name='chat_window'),
]