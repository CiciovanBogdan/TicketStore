from django.shortcuts import render
from django.views.generic import ListView
from fixture.models import FixtureMancity, FixtureRealMadrid


class FixtureListView(ListView):
    template_name = 'fixture/tickets_for_events.html'
    model = FixtureMancity
    context_object_name = 'all_fixtures'


class FixtureRealMadridListView(ListView):
    template_name = 'fixture/ticket_for_real_madrid.html'
    model = FixtureRealMadrid
    context_object_name = 'all_fixtures'


def checkout(request):
    return render(request, 'fixture/checkout.html')


def success_purchase(request):
    return render(request, 'fixture/success.html')
