from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WordsView.as_view(), name='words'),
    path('<int:pk>/', views.WordsView.as_view()),
]
