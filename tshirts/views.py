from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import TshirtForm
from .models import Tshirt


# Create your views here.


class HomePageView(ListView):
    model = Tshirt
    template_name = 'index.html'


class CreateTshirtView(CreateView):
    model = Tshirt
    form_class = TshirtForm
    template_name = 'add_tshirt.html'
    success_url = reverse_lazy('index')


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_tshirts = Tshirt.objects.all().count()

    # TODO Add brands and stories here so that they get reflected on the homepage

    context = {
        'num_tshirts': num_tshirts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
