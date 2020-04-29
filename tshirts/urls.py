from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('add/', CreateTshirtView.as_view(), name='add_tshirt'),
    path('tshirt_list/', TshirtList.as_view(), name="tshirt_list"),
    path('brand_list/', BrandsList.as_view(), name="brand_list"),
    path('story_list/', StoryList.as_view(), name="story_list"),
    path('story_list/story_detail/<int:pk>/', StoryDetail.as_view(), name="story_detail"),

]

# TODO: Implement logout https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LogoutView AND https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
