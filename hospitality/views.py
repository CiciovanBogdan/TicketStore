from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospitality.forms import HospitalityPayedForm, HospitalityVIPForm
from hospitality.models import HospitalityPayed, HospitalityVIP


# for man city
class HospitalityListView(ListView):
    template_name = 'hospitality/hospitality_payed.html'
    model = HospitalityPayed
    context_object_name = 'all_hospitality'


# for barcelona
class HospitalityBarcaListView(ListView):
    template_name = 'hospitality/hospitality_payed_barca.html'
    model = HospitalityPayed
    context_object_name = 'all_hospitality'


# for real madrid
class HospitalityVIPListView(ListView):
    template_name = 'hospitality/hospitality_vip.html'
    model = HospitalityVIP
    context_object_name = 'all_hospitality'


# for man united
class HospitalityVIPUnitedListView(ListView):
    template_name = 'hospitality/hospitality_vip_united.html'
    model = HospitalityVIP
    context_object_name = 'all_hospitality'


# for man city
class HospitalityCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = HospitalityPayed
    form_class = HospitalityPayedForm
    success_url = reverse_lazy('hospitality')


# for barcelona
class HospitalityBarcaCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = HospitalityPayed
    form_class = HospitalityPayedForm
    success_url = reverse_lazy('hospitality')


# for real madrid
class HospitalityVIPCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = HospitalityVIP
    form_class = HospitalityVIPForm
    success_url = reverse_lazy('hospitality_real')


# for man united
class HospitalityVIPUnitedCreateView(CreateView):
    template_name = 'hospitality/create_hospitality.html'
    model = HospitalityVIP
    form_class = HospitalityVIPForm
    success_url = reverse_lazy('hospitality_real')


# for man city
class HospitalityUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = HospitalityPayed
    form_class = HospitalityPayedForm
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


# for barcelona
class HospitalityBarcaUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = HospitalityPayed
    form_class = HospitalityPayedForm
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


# for real madrid
class HospitalityVIPUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = HospitalityVIP
    form_class = HospitalityVIPForm
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'


# for man united
class HospitalityVIPUnitedUpdateView(UpdateView):
    template_name = 'hospitality/update_hospitality.html'
    model = HospitalityVIP
    form_class = HospitalityVIPForm
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'


# for man city
class HospitalityDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = HospitalityPayed
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


# for barcelona
class HospitalityBarcaDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = HospitalityPayed
    success_url = reverse_lazy('hospitality')
    context_object_name = 'all_hospitality'


# for real madrid
class HospitalityVIPDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = HospitalityVIP
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'


# for man united
class HospitalityVIPUnitedDeleteView(DeleteView):
    template_name = 'hospitality/delete_hospitality.html'
    model = HospitalityVIP
    success_url = reverse_lazy('hospitality_real')
    context_object_name = 'all_hospitality'
