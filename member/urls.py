from django.urls import path

from . import views

app_name = 'member'

urlpatterns = [
    path('', views.login, name='login'),
    path('<str:uuid>/', views.profile, name='profile'),
]
