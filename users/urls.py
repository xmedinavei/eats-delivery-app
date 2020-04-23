"""Users URLs."""

# Django
from django.urls import path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from users.views import UserLoginAPIView


urlpatterns = [
    path('users/login', UserLoginAPIView.as_view(), name='login')
]
