'''Orders models.'''

# Django
from django.db import models

# Models
from users.models import User, Customer, Store
from meals.models import Meal


class Order(models.Model):
    '''Orders models.'''

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    paid = models.BooleanField(default=True) # not added payments yet

    # Status
    picked_up = models.BooleanField('picked up by the rider', default=False)
    deliveried = models.BooleanField('deliveried to customer', default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order: {}'.format(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # def __str__(self):
    #     return 'Order Item id: {}'.format(self.id)

    # def get_cost(self):
    #     return self.Meal.price * self.quantity
