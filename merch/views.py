# from functools import reduce

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from merch.forms import MerchForm
from merch.models import Merch


def get_common_data(request, context=None):
    if context is None:
        context = {}
    return context


class MerchListView(ListView):
    template_name = 'merch/merch.html'
    model = Merch
    context_object_name = 'all_merch'


class MerchCreateView(CreateView):
    template_name = 'merch/create_merch.html'
    model = Merch
    form_class = MerchForm
    success_url = reverse_lazy('merch')


class MerchUpdateView(UpdateView):
    template_name = 'merch/update_merch.html'
    model = Merch
    form_class = MerchForm
    success_url = reverse_lazy('merch')
    context_object_name = 'all_merch'


class MerchDeleteView(DeleteView):
    template_name = 'merch/delete_merch.html'
    model = Merch
    success_url = reverse_lazy('merch')
    context_object_name = 'all_merch'


class MerchDetailView(DetailView):
    template_name = 'merch/product_page.html'
    model = Merch
    context_object_name = 'all_merch'


# loc pt checkout merch
def checkout_merch(request):
    return render(request, 'checkout.html')


# de aici la real
class MerchRealListView(ListView):
    template_name = 'merch/merch_real.html'
    model = Merch
    context_object_name = 'all_merch'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = get_common_data(self.request, context)
        return context


# de aici man united
class MerchManUnitedListView(ListView):
    template_name = 'merch/merch_man_united.html'
    model = Merch
    context_object_name = 'all_merch'


# de aici barcelona
class MerchBarcelonaListView(ListView):
    template_name = 'merch/merch_barcelona.html'
    model = Merch
    context_object_name = 'all_merch'
