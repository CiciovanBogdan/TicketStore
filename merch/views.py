# from functools import reduce

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from merch.forms import MerchForm, MerchRealForm
from merch.models import Merch, MerchReal, MerchManUnited, MerchBarcelona


def get_common_data(request, context=None):
    if context is None:
        context = {}
    return context


class MerchListView(ListView):
    template_name = 'merch/merch.html'
    model = Merch
    context_object_name = 'all_merch'

    # django import-export

    # calculele se fac in views(se poate si in template)
    # def ceva(self):
    #     recepi_with_all_values = list(map(lambda recepi_ing: {'recep_ing': recepi_ing,
    #                                                           'calories': recepi_ing.quantity * recepi_ing.ingredient.calories / 100},
    #                                       recepi_ingredients))  # al doilea in care itereaza
    #     total_calories = reduce(lambda first, second: first + second['calories'], recepi_with_all_values, 0)


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


class MerchFinalDetailView(DetailView):
    template_name = 'merch/gresit_final_details.html'
    model = Merch
    context_object_name = 'all_merch'


# loc pt final details
def final_details(request):
    return render(request, 'merch/final_details.html')


# loc pt checkout merch
def checkout_merch(request):
    return render(request, 'merch/checkout_merch_city.html')


# de aici la real
class MerchRealListView(ListView):
    template_name = 'merch/merch_real.html'
    model = MerchReal
    context_object_name = 'all_merch'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context = get_common_data(self.request, context)
        return context


class MerchRealCreateView(CreateView):
    template_name = 'merch/create_merch_real.html'
    model = MerchReal
    form_class = MerchRealForm
    success_url = reverse_lazy('merch_real')


class MerchRealUpdateView(UpdateView):
    template_name = 'merch/update_merch_real.html'
    model = MerchReal
    form_class = MerchRealForm
    success_url = reverse_lazy('merch_real')
    context_object_name = 'all_merch'


class MerchRealDeleteView(DeleteView):
    template_name = 'merch/delete_merch_real.html'
    model = MerchReal
    success_url = reverse_lazy('merch_real')
    context_object_name = 'all_merch'


class MerchRealDetailView(DetailView):
    template_name = 'merch/product_page_real.html'
    model = MerchReal
    context_object_name = 'all_merch'


# de aici man united
class MerchManUnitedListView(ListView):
    template_name = 'merch/merch_man_united.html'
    model = MerchManUnited
    context_object_name = 'all_merch'


# de aici barcelona
class MerchBarcelonaListView(ListView):
    template_name = 'merch/merch_barcelona.html'
    model = MerchBarcelona
    context_object_name = 'all_merch'
