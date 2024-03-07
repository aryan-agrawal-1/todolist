from django.urls import path
from . import views

# We will define every page of our app in this variable
urlpatterns = [
    path('', views.index, name='index'),
    path('todos', views.todos, name='todos'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name="logout"),
    path('delete/<int:id>', views.delete, name='delete')
    ]

