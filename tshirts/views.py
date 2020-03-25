from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Tshirt


# Create your views here.


class HomePageView(ListView):
    model = Tshirt
    template_name = 'home.html'


class CreateTshirtView(CreateView):
    model = Tshirt
    form_class = TshirtForm
    template_name = 'add_tshirt.html'
    success_url = reverse_lazy('home')

