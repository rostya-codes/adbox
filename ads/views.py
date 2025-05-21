from django.views.generic import ListView, DetailView

from ads.models import Ad


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
