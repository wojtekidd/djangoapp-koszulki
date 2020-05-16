from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('add_tshirt/', CreateTshirtView.as_view(), name='add_tshirt'), # changed to add_tshirt
    path('tshirt_list/tshirt_detail/<int:pk>/update', UpdateTshirtView.as_view(), name='update_tshirt'),
    path('tshirt_list/tshirt_detail/<int:pk>/delete', DeleteTshirtView.as_view(), name='delete_tshirt'),
    path('add_story/', CreateStoryView.as_view(), name='add_story'), # add_story url
    path('tshirt_list/', TshirtList.as_view(), name="tshirt_list"),
    path('tshirt_detail/<int:pk>', TshirtDetail.as_view(), name="tshirt_detail"),
    path('brand_list/', BrandsList.as_view(), name="brand_list"),
    path('story_list/', StoryList.as_view(), name="story_list"),
    path('story_detail/<int:pk>/', StoryDetail.as_view(), name="story_detail"),
    path('contact/', Contact, name='contact')

]

# TODO: Implement logout https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.LogoutView AND https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
