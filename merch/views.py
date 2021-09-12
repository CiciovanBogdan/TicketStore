from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from merch.forms import MerchForm, MerchRealForm
from merch.models import Merch, MerchReal


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
