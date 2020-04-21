'''Customer model.'''

# Django
from django.db import models

# Local
from .users import User


class Customer(models.Model):
    '''Customer model.

    Customer profile hold user's public data: picture and stats.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/customers/pictures/',
        blank=True,
        null=True
    )

    delivery_address = models.TextField(max_length=200, blank=True)

    # Stats
    orders_made = models.PositiveIntegerField(default=0)

    def __str__(self):
        '''Return user's str representation.'''
        return str(self.user)

