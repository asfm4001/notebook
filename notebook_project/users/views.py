from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views, forms
from django.contrib.auth.models import User
from users.forms import RegisterForm

class RegisterCreateView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("note:list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Register"
        return context

class LoginView(views.LoginView):
    form_class = forms.AuthenticationForm
    template_name = 'users/login.html'
    # success_url = reverse_lazy("note:list")
    # LoginView 預設為 return self.get_redirect_url() or self.success_url or resolve_url(settings.LOGIN_REDIRECT_URL)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context