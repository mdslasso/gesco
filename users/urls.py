from django.urls import path, re_path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.creer_users, name='creer-users'),
    path('modifier-users.html/<int:pk>/', views.ModifierUsers.as_view(), name='modifier-users'),
    path('supprimer-users.html/<int:pk>/', views.SupprimerUsers.as_view(), name='supprimer-users'),

]
