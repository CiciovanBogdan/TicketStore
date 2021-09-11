from django.shortcuts import render


def home_page(request):
    return render(request, 'home/home_page.html')


def become_vip(request):
    return render(request, 'vip/become_vip.html')


def contact_us(request):
    return render(request, 'home/contact_us.html')


def thx_for_contact(request):
    return render(request, 'home/thx_for_cont_us.html')
