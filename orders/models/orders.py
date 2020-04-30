'''Orders models.'''

# Django
from django.db import models

# Models
from users.models import User, Customer, Store, Rider
from meals.models import Meal


class Order(models.Model):
    '''Orders models.'''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    # It will be assigned to the Order instance when the customer make the order
    rider = models.ForeignKey(
        Rider,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    paid = models.BooleanField(default=True) # not added payments yet

    # Status
    ordered= models.BooleanField(
        'Order made',
        default=False,
        help_text='Set True when the Customer wants the order to be delivered.'
    )
    picked_up = models.BooleanField(
        'picked up by the rider',
        default=False,
        help_text='Set True when the rider has picked up the order on the Store.'
    )
    deliveried = models.BooleanField(
        'deliveried to customer',
        default=False,
        help_text='Set True when the Customer has received the order.'
    )
    
    # Stats
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order id: {} Store {} Username {}'.format(
            self.id,
            self.store.name,
            self.user.username
        )

