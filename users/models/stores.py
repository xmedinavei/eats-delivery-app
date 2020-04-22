'''Store model.'''

# Django
from django.db import models

# Models
from .users import User


class Store(models.Model):
    '''Store model.

    Store profile hold user's public data: picture and stats.
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    slugname = models.SlugField(
        unique=True,
        max_length=120,
    )

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/stores/pictures/',
        blank=True,
        null=True
    )
    
    pickup_address = models.TextField(max_length=200, blank=True)

    # Stats
    orders_dispatched = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Store's reputation based on client califications"
    )

    def __str__(self):
        '''Return user's str representation.'''
        return str(self.slugname)
        
