from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Q

from .forms import TshirtForm
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


class SearchResultsView(ListView):
    model = Tshirt
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Tshirt.objects.filter(
            Q(design__icontains=query) | Q(brand__icontains=query)
        )
        return object_list


