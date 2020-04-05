from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/', CreateTshirtView.as_view(), name='add_tshirt'),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
]

