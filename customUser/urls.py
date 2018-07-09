from django.urls import path

from . import views

app_name = 'customUser'

urlpatterns = [
    path('login', views.login, name='login'),
    path('profile/<str:uuid>/', views.profile, name='profile'),
]
