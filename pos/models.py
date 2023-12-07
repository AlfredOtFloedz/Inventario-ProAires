from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
import barcode 
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from decimal import Decimal

# Create your models here.

STATUS = (
    ('PÚBLICO EN GENERAL', 'PÚBLICO EN GENERAL'),
    ('TÉCNICO', 'TÉCNICO'),
    ('PREFERENTE', 'DISTRIBUIDOR PREFERENTE'),
    ('PLUS', 'DISTRIBUIDOR PLUS'),
    ('VIP', 'DISTRIBUIDOR VIP'),
)

EQUIPO = (
    ('LIFE 12 - 1 ton 110V', 'LIFE 12 - 1 ton 110V'),  
    ('LIFE 12 - 1 ton 220V', 'LIFE 12 - 1 ton 220V'),  
    ('LIFE 12 - 1.5 ton 110V', 'LIFE 12 - 1.5 ton 110V'),  
    ('LIFE 12 - 2 ton 110V', 'LIFE 12 - 2 ton 110V'), 
    ('LIFE 12 PLUS - 1 ton 110V', 'LIFE 12 PLUS - 1 ton 110V'),  
    ('LIFE 12 PLUS - 1 ton 220V', 'LIFE 12 PLUS - 1 ton 220V'),  
    ('LIFE 12 PLUS - 1.5 ton 110V', 'LIFE 12 PLUS - 1.5 ton 110V'),  
    ('LIFE 12 PLUS - 2 ton 110V', 'LIFE 12 PLUS - 2 ton 110V'),  
    ('XLIFE - 1 ton 110V', 'XLIFE - 1 ton 110V'),  
    ('XLIFE - 1 ton 220V', 'XLIFE - 1 ton 220V'),  
    ('XLIFE - 1.5 ton 110V', 'XLIFE - 1.5 ton 110V'),  
    ('XLIFE - 2 ton 110V', 'XLIFE - 2 ton 110V'),  
    ('NEX - 1 ton 110V', 'NEX - 1 ton 110V'),  
    ('NEX - 1 ton 220V', 'NEX - 1 ton 220V'),  
    ('NEX - 1.5 ton 110V', 'NEX - 1.5 ton 110V'),  
    ('NEX - 2 ton 110V', 'NEX - 2 ton 110V'),  
    ('X32 INVERTER - 1 ton 110V', 'X32 INVERTER - 1 ton 110V'),  
    ('X32 INVERTER - 1 ton 220V', 'X32 INVERTER - 1 ton 220V'),  
    ('X32 INVERTER - 1.5 ton 110V', 'X32 INVERTER - 1.5 ton 110V'),
    ('X32 INVERTER - 2 ton 110V', 'X32 INVERTER - 2 ton 110V'), 
    ('V32 INVERTER - 1 ton 110V', 'V32 INVERTER - 1 ton 110V'),  
    ('V32 INVERTER - 1 ton 220V', 'V32 INVERTER - 1 ton 220V'),  
    ('V32 INVERTER - 1.5 ton 110V', 'V32 INVERTER - 1.5 ton 110V'),  
    ('V32 INVERTER - 2 ton 110V', 'V32 INVERTER - 2 ton 110V'),     
    ('MAGNUM 18 INV - 1 ton 110V', 'MAGNUM 18 INV - 1 ton 110V'),  
    ('MAGNUM 22 INV - 1 ton 110V', 'MAGNUM 22 INV - 1 ton 110V'),  
    ('MAGNUM 22 INV - 1 ton 220V', 'MAGNUM 22 INV - 1 ton 220V'),  
    ('MAGNUM 22 INV - 1.5 ton 110V', 'MAGNUM 22 INV - 1.5 ton 110V'),  
    ('MAGNUM 22 INV - 2 ton 110V', 'MAGNUM 22 INV - 2 ton 110V'), 
    ('MAGNUM 21 PLATINUM - 1 ton 110V', 'MAGNUM 21 PLATINUM - 1 ton 110V'),  
    ('MAGNUM 21 PLATINUM - 1 ton 220V', 'MAGNUM 21 PLATINUM - 1 ton 220V'),  
    ('X-ONE - 1 ton 110V', 'X-ONE - 1 ton 110V')
)

FACTURACION =(
    ('Cliente','Cliente'),
    ('PUBLICO EN GENERAL','PÚBLICO EN GENERAL')
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

class Pos_Equipo(models.Model):
    equipo = models.CharField(max_length=100, choices=EQUIPO)
    cantidad = models.PositiveIntegerField(default=1)
    precio_u = models.PositiveIntegerField()
    descuento = models.DecimalField(max_digits=100, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Equipos'
        
    @property
    def precio_iva(self):  
        return round(self.precio_u * Decimal(1-(self.descuento/100)) * Decimal(1.16), 2)
    
    @property
    def precio_gral(self):
        if self.equipo == 'LIFE 12 - 1 ton 110V' or self.equipo == 'LIFE 12 - 1 ton 220V' or self.equipo == 'LIFE 12 PLUS - 1 ton 110V' or self.equipo == 'LIFE 12 PLUS - 1 ton 220V':
            return round(self.precio_iva * Decimal(1.3397))
        elif self.equipo == 'LIFE 12 - 1.5 ton 110V' or self.equipo == 'LIFE 12 PLUS - 1.5 ton 110V':
            return round(self.precio_iva * Decimal(1.2797))
        elif self.equipo == 'LIFE 12 - 2 ton 110V' or self.equipo == 'LIFE 12 PLUS - 2 ton 110V':
            return round(self.precio_iva * Decimal(1.2378))
        else:
            return round(self.precio_iva * Decimal(1.2245))
    
    @property
    def precio_tec(self):
        return round(self.precio_gral * Decimal(1-0.0659),2)
    
    @property
    def precio_d1(self):
        return round(self.precio_tec * Decimal(1-0.03),2)
    
    @property
    def precio_d2(self):
        return round(self.precio_tec * Decimal(1-0.05),2)
    
    @property
    def precio_d3(self):
        return round(self.precio_tec * Decimal(1-0.08),2)
    
    def __str__(self):
        return f'{self.equipo}--{self.cantidad} Disponibles.'
    