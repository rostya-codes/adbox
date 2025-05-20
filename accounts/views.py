from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.forms import RegisterForm


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


class CustomLogoutView(LogoutView):
    next_page = 'login'
