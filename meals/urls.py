"""Meals URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from meals.views import meals as meals_views


router = DefaultRouter()
router.register(
    r'stores/(?P<store_slugname>[a-zA-Z0-9]+)/meals',
    meals_views.MealViewSet,
    basename='meals'
)



urlpatterns = [
    path('', include(router.urls))
]
