from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospitality.forms import HospitalityForm, HospitalityRealForm
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


class HospitalityRealCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = HospitalityReal
    form_class = HospitalityRealForm
    success_url = reverse_lazy('hospitality_real')


class HospitalityUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = Hospitality
    form_class = HospitalityForm
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


class HospitalityRealUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = HospitalityReal
    form_class = HospitalityRealForm
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'


class HospitalityDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = Hospitality
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


class HospitalityRealDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = HospitalityReal
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'
