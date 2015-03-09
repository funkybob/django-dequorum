from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import User


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'registration/register.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(User.objects.make_random_password())
        obj.save()
        return redirect('accounts:register-password')
