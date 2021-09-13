from django.shortcuts import render

from fixture.models import FixtureMancity
from hospitality.models import Hospitality
from merch.models import Merch, MerchReal


def home_page(request):
    return render(request, 'home/home_page.html')


def become_vip(request):
    return render(request, 'vip/become_vip.html')


def contact_us(request):
    return render(request, 'home/contact_us.html')


def thx_for_contact(request):
    return render(request, 'home/thx_for_cont_us.html')


def search_page_view(request):
    search = request.GET.get('search')
    merch_found = Merch.objects.filter(name__contains=search)
    # another_product = Merch.objects.filter()
    # merch_found = list(merch_found)
    # another_product = list(another_product)
    # merch_found.extend(another_product)
    return render(request, 'merch/merch.html', {'all_merch': merch_found})


def search_madrid_view(request):
    search = request.GET.get('search')
    merch_real = MerchReal.objects.filter(name__contains=search)
    return render(request, 'merch/merch_real.html', {'all_merch': merch_real})


def search_hospitality_view(request):
    search = request.GET.get('search')
    hospitality_found = Hospitality.objects.filter(name__contains=search)
    return render(request, 'hospitality/hospitality.html', {'all_hospitality': hospitality_found})


# def search_hospitality_real_view(request):
#     search = request.GET.get('search')
#     hospitality_found = HospitalityReal.objects.filter(name__contains=search)
#     return render(request, 'hospitality/hospitality_real.html', {'all_hospitality': hospitality_found})

def search_fixture_view(request):
    search = request.GET.get('search')
    fixture_found = FixtureMancity.objects.filter(title__contains=search)
    return render(request, 'fixture/tickets_for_events.html',
                  {'all_fixture': fixture_found})  # aici este o problema mare
