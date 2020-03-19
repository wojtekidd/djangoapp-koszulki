from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", startpage_response),
    path("info", infopage_response),
    path("list", movielist_response, name='movie_list'),
    path("add", movieadd_response, name='movie_add'),
    path("movieedit/<int:id>", movieedit_response, name='movie_edit'),
    path("moviedel/<int:id>", moviedel_response, name='movie_del'),
    path("list/<int:id>", moviedetails_response, name='movie_details'),
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout", auth_views.LogoutView.as_view(), name='logout'),
    path("logout-done", logout_done, name='logout-done'),
]