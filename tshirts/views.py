from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .forms import TshirtForm, StoryForm
from .models import Tshirt, Story

# Create your views here.

class HomePageView(ListView):
    model = Tshirt
    template_name = 'index.html'

    def get_context_data(self):
        # Call the base implementation first to get a context
        context = super().get_context_data()
        # Add in a QuerySet of all the Tshirts, referable as num_shirts
        context['num_tshirts'] = Tshirt.objects.all().count()
        # queryset for all uniqe Tshirt items of the brand column
        context['num_brands'] = Tshirt.objects.values('brand').distinct().count()
        # this line below counts the number of existing stories
        context['num_stories'] = Story.objects.all().count()
        return context


class CreateTshirtView(CreateView):
    model = Tshirt
    form_class = TshirtForm
    template_name = 'add_tshirt.html'
    success_url = reverse_lazy('index')


class CreateStoryView(CreateView):
    """
    a sepearate view for adding story
    """
    model = Story
    form_class = StoryForm
    template_name = 'add_story.html'
    success_url = reverse_lazy('index')


class TshirtList(ListView):
    """
    Draws a list of all t-shirts from db.
    """
    model = Tshirt
    template_name = 'tshirt_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['tshirts'] = Tshirt.objects.all()
        return context


class TshirtDetail(TemplateView):
    """
    Creates a detailed view (all relevant objects, stories and t-shirt items) of a t-shirt from db.
    """
    # model = Tshirt
    context_object_name = "tshirt_detail"
    template_name = "tshirt_detail.html"
    # queryset = Tshirt.objects.all()


    # def get(self, request, pk):
    #     id = pk
    #     tshirt_items = get_object_or_404(Tshirt)
    #     story_items = Story.objects.filter(story=tshirt_items)
    #     return render(self.request, "tshirt_detail.html", {"tshirt": tshirt_items, "story": story_items})

    #
    # def get_queryset(self):
    #     # all_objects = tshirt_objects | story_objects
    #     return tshirt_items

    def get_context_data(self, **kwargs):
        context = super(TshirtDetail, self).get_context_data(**kwargs)
        context['tshirts'] = Tshirt.objects.all() # creates queryset of all Tshirt items referable as tshirts
        context['stories'] = Story.objects.all()
        return context


class BrandsList(ListView):
    model = Tshirt
    template_name = 'brand_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['brands'] = Tshirt.objects.values('brand').distinct()
        return context


class StoryList(ListView):
    """
    Draws a list of all stories from db.
    """
    model = Story
    template_name = 'story_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['stories'] = Story.objects.all()
        return context


class StoryDetail(DetailView):
    """
    Pulls a detailed view (content) of a story from db.
    """
    model = Story
    template_name = "story_detail.html"

    def get_queryset(self):
        return Story.objects