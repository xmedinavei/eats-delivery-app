'''Orders models.'''

# Django
from django.db import models

# Models
from users.models import Customer, Store
from meals.models import Meal


class Order(models.Model):
    '''Orders models.'''

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=True) # not added payments yet


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order: {}'.format(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return 'Order Item id: {}'.format(self.id)

    # def get_cost(self):
    #     return self.Meal.price * self.quantity
