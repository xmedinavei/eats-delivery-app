"""Orders URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from orders.views import orders as orders_views


router = DefaultRouter()
router.register(
    r'users/(?P<username>[a-zA-Z0-9]+)/customer/orders',
    orders_views.OrderViewSet,
    basename='orders'
)



urlpatterns = [
    path('', include(router.urls))
]
