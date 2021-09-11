from django.shortcuts import render
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from fixture.models import FixtureMancity, FixtureRealMadrid


class FixtureListView(ListView):
    template_name = 'ticket/tickets_for_events.html'
    model = FixtureMancity
    context_object_name = 'all_fixtures'


class FixtureRealMadridListView(ListView):
    template_name = 'ticket/ticket_for_real_madrid.html'
    model = FixtureRealMadrid
    context_object_name = 'all_fixtures'


def success(request, uid):
    template = render_to_string('ticket/email_template.html', {'name': request.user.username})

    email = EmailMessage(
        'Ticket purchase successfully',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )

    email.fail_silently = False
    email.send()

    project = FixtureMancity.objects.get(id=uid)
    context = {'project': project}

    return render(request, 'ticket/success.html', context)


def checkout(request):
    return render(request, 'ticket/checkout.html')


def success_purchase(request):
    return render(request, 'ticket/success.html')
