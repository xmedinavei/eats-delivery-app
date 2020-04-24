"""Users URLs."""

# Django
from django.urls import path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from users.views import (
    UserLoginAPIView,
    UserSignUpAPIView,
    AccountVerificationAPIView
)


urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]
