from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospitality.forms import HospitalityForm
from hospitality.models import Hospitality, HospitalityReal


class HospitalityListView(ListView):
    template_name = 'hospitality/hospitality.html'
    model = Hospitality
    context_object_name = 'all_hospitality'


class HospitalityRealListView(ListView):
    template_name = 'hospitality/hospitality_real.html'
    model = HospitalityReal
    context_object_name = 'all_hospitality'


class HospitalityCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = Hospitality
    form_class = HospitalityForm
    success_url = reverse_lazy('hospitality')


class HospitalityUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = Hospitality
    form_class = HospitalityForm
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitalitys'


class HospitalityDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = Hospitality
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitalitys'
