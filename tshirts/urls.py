from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('add/', CreateTshirtView.as_view(), name='add_tshirt'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]

# TODO: Implement logout https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LogoutView AND https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
