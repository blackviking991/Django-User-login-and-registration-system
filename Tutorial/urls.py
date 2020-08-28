from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]
