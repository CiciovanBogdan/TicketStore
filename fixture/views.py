from django.shortcuts import render
from django.views.generic import ListView
from fixture.models import Fixture


class FixtureListView(ListView):
    template_name = 'fixture/tickets_for_events.html'
    model = Fixture
    context_object_name = 'all_fixtures'


class FixtureRealMadridListView(ListView):
    template_name = 'fixture/ticket_for_real_madrid.html'
    model = Fixture
    context_object_name = 'all_fixtures'


class FixtureManUnitedListView(ListView):
    template_name = 'fixture/ticket_for_man_united.html'
    model = Fixture
    context_object_name = 'all_fixtures'


class FixtureBarcelonaListView(ListView):
    template_name = 'fixture/ticket_for_fc_barcelona.html'
    model = Fixture
    context_object_name = 'all_fixtures'


def checkout(request):
    return render(request, 'fixture/checkout.html')


def success_purchase(request):
    return render(request, 'fixture/success.html')


def reduce_price():
    pass
