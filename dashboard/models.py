from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from pos.models import Customer
# Create your models here.

CATEGORY = (
    ('1', 'Condensadora'),
    ('2', 'Evaporadora'),
    ('3', 'Boiler'),
)

class Producto(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    type = models.CharField(max_length=100, default=None)
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=1000.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    price_update = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}--{self.code}'

class Order(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE)
    order_quantity = models.PositiveBigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f'{self.product} pedido realizado por {self.staff.username}'