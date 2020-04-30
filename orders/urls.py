"""Orders URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from orders.views import orders as orders_views
from orders.views import order_items as order_items_views


router = DefaultRouter()
router.register(
    r'users/(?P<username>[a-zA-Z0-9]+)/stores/(?P<store_slugname>[a-zA-Z0-9]+)/orders',
    orders_views.OrderViewSet,
    basename='orders'
)
router.register(
    r'users/(?P<username>[a-zA-Z0-9]+)/stores/(?P<store_slugname>[a-zA-Z0-9]+)/orders/(?P<uid>[0-9]+)/meal/(?P<slugname>[a-zA-Z0-9]+)',
    order_items_views.OrderItemViewSet,
    basename='order_items'
)



urlpatterns = [
    path('', include(router.urls))
]
