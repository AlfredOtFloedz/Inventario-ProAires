from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PAYMENT = (
    ('cash', 'Efectivo'),
    ('card', 'Tarjeta'),
    ('transaction','Tranferencia'),
)

STATUS = (
    ('PÚBLICO EN GENERAL', 'PÚBLICO EN GENERAL'),
    ('PREFERENTE', 'DISTRIBUIDOR PREFERENTE'),
    ('PLUS', 'DISTRIBUIDOR PLUS'),
    ('VIP', 'DISTRIBUIDOR VIP'),
)

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS)
    RFC = models.CharField(max_length=100)
    DIR = models.CharField(max_length=100)
    CFDI = models.CharField(max_length=100)
    REG_FIS = models.CharField(max_length=100)
    c_email = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=100)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')

    class Meta:
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f'{self.customer_name}'