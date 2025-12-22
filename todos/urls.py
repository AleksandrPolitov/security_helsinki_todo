from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('toggle/<int:todo_id>/', views.toggle, name='toggle'),

    # FIX (3): Add login and logout views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

