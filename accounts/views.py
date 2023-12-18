from django.views.generic.edit import CreateView
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

@login_required
def logout_user(request):
    logout(request)
    return redirect('index')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')