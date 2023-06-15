from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import User
from django.db.models import Sum

class Basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class PizzaCategory(Basemodel):
    category_name = models.CharField(max_length=100)

class Pizza(Basemodel):
    category = models.ForeignKey(PizzaCategory, on_delete=models.CASCADE, related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    images = models.ImageField(upload_to='pizza')
    description=models.CharField(max_length=500)

class Cart(Basemodel):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='carts')
    is_paid = models.BooleanField(default=False)
    def get_cart_total(self):
        return CartItems.objects.filter(cart=self).aggregate(Sum('pizza__price'))['pizza__price__sum']

class CartItems(Basemodel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

class Details(Basemodel):
    detail_name=models.CharField(max_length=100)
    link=models.CharField(max_length=100)

class Card(Basemodel):
    images=models.ImageField(upload_to='card')
    text=models.CharField(max_length=100)

class Offers(Basemodel):
    offer_title=models.CharField(max_length=100)
    offer_description=models.CharField(max_length=500)
    offer_tc=models.CharField(max_length=500)

    

