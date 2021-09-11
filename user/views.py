from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'user/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('home_page')
