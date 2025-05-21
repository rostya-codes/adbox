from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdsListView.as_view(), name='ads-list'),
    path('details/<int:pk>/', views.AdDetailView.as_view(), name='ad-detail'),
]
