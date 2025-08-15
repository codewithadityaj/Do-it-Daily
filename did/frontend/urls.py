from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('index/', views.index_page, name='index'),
    path('child/', views.child_page, name='child'),
    path('teen/', views.teen_page, name='teen'),
    path('adult/', views.adult_page, name='adult'),
    path('child/rewards/', views.child_rewards_page, name='child_rewards'),
    path('child/progress/', views.child_progress_page, name='child_progress'),
    path('child/challenges/', views.child_challenge_page, name='child_challenge'),
]
