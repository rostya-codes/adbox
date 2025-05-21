from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import CreateView

from accounts.forms import RegisterForm

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        Перевіряє, чи користувач вже авторизований.
        Якщо так — автоматично перенаправляє на success_url,
        щоб уникнути показу сторінки логіну або реєстрації для авторизованих.
        Це покращує UX і запобігає зайвому доступу.
        """
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        """
        Перевіряє, чи користувач вже авторизований.
        Якщо так — автоматично перенаправляє на success_url,
        щоб уникнути показу сторінки логіну або реєстрації для авторизованих.
        Це покращує UX і запобігає зайвому доступу.
        """
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'username')
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')
    context_object_name = 'user'

    def get_object(self, queryset=None):  # Явне вимкнення використання queryset
        return self.request.user


class CustomLogoutView(LogoutView):
    next_page = 'login'
