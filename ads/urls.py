from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAdView.as_view(), name='create-ad'),
    path('', views.AdsListView.as_view(), name='ads-list'),
    path('details/<int:pk>/', views.AdDetailView.as_view(), name='ad-detail'),
    path('update/<int:pk>/', views.UpdateAdView.as_view(), name='update-ad'),
    path('delete/<int:pk>/', views.DeleteAdView.as_view(), name='delete-ad'),
]
