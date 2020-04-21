'''Client model.'''

# Django
from django.db import models


class Client:
    '''Client model.

    Client profile hold user's public data: picture, bio and stats.
    '''

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    delivery_address = models.TextField(max_length=200, blank=True)

    # Stats
    orders_made = models.PositiveIntegerField(default=0)

    def __str__(self):
        '''Return user's str representation.'''
        return str(self.user)

