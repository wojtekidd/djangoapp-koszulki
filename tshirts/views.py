from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import *
from .models import Tshirt


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


# Contact form-view
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
            ['damiann.szymanski@gmail.com'],
            headers= {'Reply to': contact_email}
        )

        email.send()

        return redirect('index')

    return render(request, 'contact.html', {'form': Contact_Form})