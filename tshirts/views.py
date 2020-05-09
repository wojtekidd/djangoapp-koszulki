from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import TshirtForm
from .models import Tshirt, Story


# Create your views here.

class HomePageView(ListView):
    model = Tshirt
    template_name = 'index.html'

    def get_context_data(self):
        # Call the base implementation first to get a context
        context = super().get_context_data()
        # Add in a QuerySet of all the Tshirts
        context['num_tshirts'] = Tshirt.objects.all().count()
        return context


class CreateTshirtView(CreateView):
    model = Tshirt
    form_class = TshirtForm
    template_name = 'add_tshirt.html'
    success_url = reverse_lazy('index')


class TshirtList(ListView):
    model = Tshirt
    template_name = 'tshirt_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['tshirts'] = Tshirt.objects.all()
        return context


class BrandsList(ListView):
    model = Tshirt
    template_name = 'brand_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['brands'] = Tshirt.objects.all()
        return context


class StoryList(ListView):
    model = Story
    template_name = 'story_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['stories'] = Story.objects.all()
        return context


class StoryDetail(DetailView):
    model = Story
    template_name = "story_detail.html"

    def get_queryset(self):
        return Story.objects