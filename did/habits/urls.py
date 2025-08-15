# habits/urls.py

from django.urls import path
from .views import HabitListCreateView, HabitDetailView


urlpatterns = [
    path('', HabitListCreateView.as_view(), name='habit_list_create'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),

]
