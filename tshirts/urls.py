from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/', CreateTshirtView.as_view(), name='add_tshirt')
]
