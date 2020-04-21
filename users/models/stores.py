'''Store model.'''

# Django
from django.db import models

# Local
from .users import User


class Store(models.Model):
    '''Store model.

    Store profile hold user's public data: picture and stats.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    picture = models.ImageField(
        'profile picture',
        upload_to='users/stores/pictures/',
        blank=True,
        null=True
    )
    
    store_address = models.TextField(max_length=200, blank=True)

    # Stats
    orders_dispatched = models.PositiveIntegerField(default=0)
    store_reputation = models.FloatField(
        default=5.0,
        help_text="Store's reputation based on client califications"
    )

    def __str__(self):
        '''Return user's str representation.'''
        return str(self.user)
