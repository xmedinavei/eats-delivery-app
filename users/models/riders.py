'''Rider model.'''

# Django
from django.db import models
from django.core.validators import RegexValidator


class Rider(models.Model):
    '''Rider model.

    Rider profile hold user's public data: picture and stats.
    '''

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # is_rider = models.BooleanField(default=True)

    # Auth to Users will be implemented
    #####################
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ######################

    picture = models.ImageField(
        'profile picture',
        upload_to='users/riders/pictures/',
        blank=True,
        null=True
    )

    # Motorcicle
    vehicle_made = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    # Regex validator for motorcicle licence plate
    licence_plate_regex = RegexValidator(
        regex=r'^\w{2}\d{3}\w$',
        message="Motorcicle  licence plate must be entered in the format: AA111A"
    )
    licence_plate = models.CharField(
        validators=[licence_plate_regex], max_length=6,
        unique=True,
    )

    location = models.TextField(max_length=200, blank=True)

    # Status
    orders_active = models.SmallIntegerField(
        '# orders assigned to delivery',
        default=0,
        help_text="Number of orders assigned to deliver."
    )
    is_available = models.BooleanField(
        'Is the rider available to deliver?',
        default=True,
        help_text="When orders_active==2, this set to False."
    )
    is_active = models.BooleanField(
        'Is the account active?',
        default=True,
        help_text="True: account active. False: inactive."
    )

    # Stats
    orders_dispatched = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Rider's reputation based on client califications"
    )


    class Meta:
        ordering = ['-id']


    def __str__(self):
        '''Return user's str representation.'''
        return str(f'ID: {self.id}, first name: {self.first_name}, last_name: {self.last_name}')
