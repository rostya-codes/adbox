from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from .forms import CreateAdForm, UpdateAdForm


class DashboardView(ListView):
    model = Ad
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'ads'

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user).order_by('-created_at')


class CreateAdView(CreateView):
    model = Ad
    form_class = CreateAdForm
    template_name = 'dashboard/create-ad.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user  # form.instance — це створений об’єкт Ad, але ще не збережений.
        return super().form_valid(form)


class UpdateAdView(UpdateView):
    model = Ad
    template_name = 'dashboard/update-ad.html'
    form_class = UpdateAdForm
    success_url = reverse_lazy('dashboard')


class DeleteAdView(DeleteView):
    model = Ad
    template_name = 'dashboard/delete-ad.html'
    context_object_name = 'ad'
    success_url = reverse_lazy('dashboard')
