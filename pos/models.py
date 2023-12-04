from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
import barcode 
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.

STATUS = (
    ('PÚBLICO EN GENERAL', 'PÚBLICO EN GENERAL'),
    ('TÉCNICO', 'TÉCNICO'),
    ('PREFERENTE', 'DISTRIBUIDOR PREFERENTE'),
    ('PLUS', 'DISTRIBUIDOR PLUS'),
    ('VIP', 'DISTRIBUIDOR VIP'),
)

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS)
    RFC = models.CharField(max_length=100, unique=True)
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

class CustomerID(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    barcode = models.ImageField(upload_to='Profile_Images', blank=True)
    
    def __str__(self):
        return str(self.customer)
    
    def save(self, *args, **kwargs):
        Code128 = barcode.get_barcode_class('code128')
        code = Code128(f'{self.customer.RFC}', writer=ImageWriter())
        buffer = BytesIO()
        code.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)

