from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import *
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


"""Contact form-view"""
def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

        template = get_template('contact_form.txt')

        content = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'contact_content': contact_content
        }

        content = template.render(content)

        email = EmailMessage(
            "New contact form",
            content,
            "KoszulkiApp" + '',
            ['koszulkistore@gmail.com'],
            headers= {'Reply to': contact_email}
        )

        email.send()

        return redirect('index')

    return render(request, 'contact.html', {'form': Contact_Form})