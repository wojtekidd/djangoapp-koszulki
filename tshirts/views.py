from django.views.generic import ListView
from .models import Tshirt

# Create your views here.


class HomePageView(ListView):
    model = Tshirt
    template_name = 'home.html'
