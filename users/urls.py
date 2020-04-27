"""Users URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from users.views import users as user_views
from users.views import stores as stores_views
from users.views import riders as riders_views


router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'stores', stores_views.StoreViewSet, basename='stores')
router.register(r'riders', riders_views.RiderViewSet, basename='riders')


urlpatterns = [
    path('', include(router.urls))
]
