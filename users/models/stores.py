'''Store model.'''

# Django
from django.db import models


class Store(models.Model):
    '''Store model.

    Store profile hold user's public data: picture and stats.
    '''

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # is_store = models.BooleanField(default=True)

    name = models.CharField(max_length=120)
    store_slugname = models.SlugField(
        unique=True,
        max_length=120,
    )

    about = models.CharField('circle description', max_length=255, blank=True)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/stores/pictures/',
        blank=True,
        null=True
    )
    
    pickup_address = models.TextField(max_length=200)

    # Status
    is_active = models.BooleanField(
        'active or inactive account',
        default=True,
        help_text='Account acctive or inactive.'
    )
    is_open = models.BooleanField(
        'Store working or not',
        default=True,
        help_text='Store working or close'
    )

    # Stats
    orders_dispatched = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Store's reputation based on client califications"
    )


    class Meta:
        ordering = ['-id']


    def __str__(self):
        '''Return user's str representation.'''
        return str(self.store_slugname)
        
