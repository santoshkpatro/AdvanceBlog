from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:user_id>/dashboard/', views.dashboard, name='dashboard'),
    path('<str:user_id>/post/', views.post, name='post'),
]