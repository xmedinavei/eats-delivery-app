'''eatsapp URL Configuration.

Users viewset
#######################################################################################################################################
    Http methods and the URLs:

    POST            /users/signup/                  (After signup, token is sent to the terminal as emailconfirmation)
    POST            /users/verify/                  (Sent the token as data to verify the account)
    POST            /users/login/                   (After login, access_token is provided)
    GET             /users/<username>/  *           (show User and Customer detail)
    PUT or PATCH    /users/<username>/  *
    PUT or PATCH    /users/<username>/customer/  *

    * : access_token must be provided in the headers as: "Authorization: Token <acces_token>
        access_token is provided in the login.
########################################################################################################################################

Stores viewset
########################################################################################################################################
    Http methods and the URLs:

    GET             /stores/                        (list Stores)
    POST            /stores/                        (create Store)
    PUT             /stores/                        (update Store info)
    PATCH           /stores/                        (partial update Store info
    GET            /stores/<id>/orders/             (show Orders not pickup yet)
########################################################################################################################################

Riders viewset
########################################################################################################################################
    Http methods and the URLs:

    GET             /riders/                        (list Riders)
    POST            /riders/                        (create Rider)
    PUT             /riders/                        (update Rider info)
    PATCH           /riders/                        (partial Rider Store info)
    GET             /riders/<id>/orders/            (show orders to pickup)
########################################################################################################################################

Meals viewset
########################################################################################################################################
    Http methods and the URLs:

    GET             /stores/<store_slugname>/meals/         (list Store meals)
    POST            /stores/<store_slugname>/meals/         (create Stores meal)
########################################################################################################################################

Orders viewset
########################################################################################################################################
    Http methods and the URLs:

    GET         /users/<username>/stores/<store_slugname>/orders/                   (list Customer's order from a Store)
    POST        /users/<username>/stores/<store_slugname>/orders/                   (create) # DO NOT SEND DATA TO CREATE AN ORDER
    POST        /users/<username>/stores/<store_slugname>/orders/<id>/make_order/   (make order and assign a Rider)
#########################################################################################################################################

OrderItems viewset
##########################################################################################################################################
    Http methods and the URLs:

    POST        users/<username>/stores/<store_slugname>/orders/<uid>/meal/<slugname>/       (Insert Meal into an existing User's Order )
##########################################################################################################################################
'''

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Django admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('meals.urls', 'meals'), namespace='meals')),
    path('', include(('orders.urls', 'orders'), namespace='orders'))
]
