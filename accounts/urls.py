from django.urls import path
from .import views

urlpatterns = [
    path('userlogin/', views.userlogin, name='userlogin'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]