from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from fixture.models import Fixture
from home.forms import VIPForm
from home.models import VIP
from hospitality.models import HospitalityPayed, HospitalityVIP
from merch.models import Merch


def home_page(request):
    return render(request, 'home/home_page.html')


class BecomeVIPListView(ListView):
    template_name = 'home/become_vip.html'
    model = VIP
    context_object_name = 'all_vip'


class VIPCreateView(CreateView):
    template_name = 'home/create_vip.html'
    model = VIP
    form_class = VIPForm
    success_url = reverse_lazy('become_vip')
    context_object_name = 'all_vip'


class VIPUpdateView(UpdateView):
    template_name = 'home/update_vip.html'
    model = VIP
    form_class = VIPForm
    success_url = reverse_lazy('become_vip')
    context_object_name = 'all_vip'


class VIPDeleteView(DeleteView):
    template_name = 'home/delete_vip.html'
    model = VIP
    success_url = reverse_lazy('become_vip')
    context_object_name = 'all_vip'


def add_to_member(request):
    group = Group.objects.get(name='Member')
    user = request.user.id
    group.user_set.add(user)
    return render(request, 'home/vip_activation_success.html')


def remove_from_member(request):
    group = Group.objects.get(name='Member')
    user = request.user.id
    group.user_set.remove(user)
    return render(request, 'home/cancel_vip_sub.html')


def checkout_vip(request):
    return render(request, 'home/checkout_vip.html')


def contact_us(request):
    return render(request, 'home/contact_us.html')


def thx_for_contact(request):
    return render(request, 'home/thx_for_cont_us.html')


def search_merch_city(request):
    search = request.GET.get('search')
    merch_found = Merch.objects.filter(name__contains=search)
    return render(request, 'merch/merch.html', {'all_merch': merch_found})


def search_merch_real(request):
    search = request.GET.get('search')
    merch_found = Merch.objects.filter(name__contains=search)
    return render(request, 'merch/merch_real.html', {'all_merch': merch_found})


def search_merch_united(request):
    search = request.GET.get('search')
    merch_found = Merch.objects.filter(name__contains=search)
    return render(request, 'merch/merch_man_united.html', {'all_merch': merch_found})


def search_merch_barcelona(request):
    search = request.GET.get('search')
    merch_found = Merch.objects.filter(name__contains=search)
    return render(request, 'merch/merch_barcelona.html', {'all_merch': merch_found})


def search_hospitality_payed(request):
    search = request.GET.get('search')
    hospitality_found = HospitalityPayed.objects.filter(name__contains=search)
    return render(request, 'hospitality/hospitality_payed.html', {'all_hospitality': hospitality_found})


def search_hospitality_vip(request):
    search = request.GET.get('search')
    hospitality_found = HospitalityVIP.objects.filter(name__contains=search)
    return render(request, 'hospitality/hospitality_vip.html', {'all_hospitality': hospitality_found})


def search_fixture_city(request):
    search = request.GET.get('search')
    fixture_found = Fixture.objects.filter(title_man_city__contains=search)
    return render(request, 'fixture/tickets_for_events.html', {'all_fixtures': fixture_found})


def search_fixture_real(request):
    search = request.GET.get('search')
    fixture_found = Fixture.objects.filter(title_real_madrid__contains=search)
    return render(request, 'fixture/ticket_for_real_madrid.html', {'all_fixtures': fixture_found})


def search_fixture_man_united(request):
    search = request.GET.get('search')
    fixture_found = Fixture.objects.filter(title_man_united__contains=search)
    return render(request, 'fixture/ticket_for_man_united.html', {'all_fixtures': fixture_found})


def search_fixture_barcelona(request):
    search = request.GET.get('search')
    fixture_found = Fixture.objects.filter(title_barcelona__contains=search)
    return render(request, 'fixture/ticket_for_fc_barcelona.html', {'all_fixtures': fixture_found})
