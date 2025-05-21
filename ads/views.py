from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from ads.forms import CreateAdForm
from ads.models import Ad

"""
Так, загалом це основне, що потрібно налаштувати в цих класах:

    model — яка модель буде оброблятися.

    fields або form_class — які поля форми показувати або власна форма (якщо є).

    template_name — шаблон, який вьюха буде рендерити (якщо не хочеш використовувати дефолтні імена).

    success_url — куди переадресувати після успішної операції (створення, редагування, видалення).

Крім того, можеш додати:

    context_object_name — щоб у шаблоні звертатися до об’єкта через більш зрозуміле ім’я.

    Перевизначення методів типу get_queryset(), get_object() чи form_valid() — для кастомної логіки.
"""

class CreateAdView(CreateView):
    model = Ad
    form_class = CreateAdForm
    template_name = 'ads/create-ad.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user  # form.instance — це створений об’єкт Ad, але ще не збережений.
        return super().form_valid(form)


class AdsListView(ListView):
    model = Ad
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class UpdateAdView(UpdateView):
    pass


class DeleteAdView(DeleteView):
    pass
