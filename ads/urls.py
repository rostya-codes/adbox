from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAdView.as_view(), name='create-ad'),
    path('', views.AdsListView.as_view(), name='ads-list'),
    path('details/<int:ad_id>/', views.AdDetailsView.as_view(), name='ad-details'),
    path('update/<int:ad_id>/', views.UpdateAdView.as_view(), name='update-ad'),
    path('delete/<int:ad_id>/', views.DeleteAdView.as_view(), name='delete-ad'),
]
