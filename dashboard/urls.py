from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAdView.as_view(), name='create-ad'),  # Create
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # Read
    path('update/<int:pk>/', views.UpdateAdView.as_view(), name='update-ad'),  # Update
    path('delete/<int:pk>/', views.DeleteAdView.as_view(), name='delete-ad'),  # Delete
]
