'''eatsapp URL Configuration.'''

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users'))
]
