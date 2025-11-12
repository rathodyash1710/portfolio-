from django.urls import path
from .views import PortfolioView, ProfileDetailView

urlpatterns = [
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
]