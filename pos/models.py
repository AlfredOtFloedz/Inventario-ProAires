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
    ('INVERTER 17 - 1 ton 110V', 'INVERTER 17 - 1 ton 110V'),
    ('INVERTER 17 - 1 ton 220V', 'INVERTER 17 - 1 ton 220V'),
    ('INVERTER 17 - 1.5 ton 220V', 'INVERTER 17 - 1.5 ton 220V'),
    ('INVERTER 17 - 2 ton 220V', 'INVERTER 17 - 2 ton 220V'),
    ('INVERTER 17 - 3 ton 220V', 'INVERTER 17 - 3 ton 220V'),
    ('INVERTER X - 1 ton 110V', 'INVERTER X - 1 ton 110V'),
    ('INVERTER X - 1 ton 220V', 'INVERTER X - 1 ton 220V'),
    ('INVERTER X - 1.5 ton 220V', 'INVERTER X - 1.5 ton 220V'),
    ('INVERTER X - 2 ton 220V', 'INVERTER X - 2 ton 220V'),
    ('LIFE 12 - 1 ton 110V', 'LIFE 12 - 1 ton 110V'),  
    ('LIFE 12 - 1 ton 220V', 'LIFE 12 - 1 ton 220V'),  
    ('LIFE 12 - 1.5 ton 220V', 'LIFE 12 - 1.5 ton 220V'),  
    ('LIFE 12 - 2 ton 220V', 'LIFE 12 - 2 ton 220V'), 
    ('LIFE 12 PLUS - 1 ton 110V', 'LIFE 12 PLUS - 1 ton 110V'),  
    ('LIFE 12 PLUS - 1 ton 220V', 'LIFE 12 PLUS - 1 ton 220V'),  
    ('LIFE 12 PLUS - 1.5 ton 220V', 'LIFE 12 PLUS - 1.5 ton 220V'),  
    ('LIFE 12 PLUS - 2 ton 220V', 'LIFE 12 PLUS - 2 ton 220V'),  
    ('MAGNUM 18 INV - 3 ton 220V', 'MAGNUM 18 INV - 3 ton 220V'),
#    ('MAGNUM 21 PLATINUM - 1 ton 220V', 'MAGNUM 21 PLATINUM - 1 ton 110V'),  
#    ('MAGNUM 21 PLATINUM - 1 ton 220V', 'MAGNUM 21 PLATINUM - 1 ton 220V'),    
    ('MAGNUM 22 INV - 1 ton 110V', 'MAGNUM 22 INV - 1 ton 110V'),  
    ('MAGNUM 22 INV - 1 ton 220V', 'MAGNUM 22 INV - 1 ton 220V'),  
    ('MAGNUM 22 INV - 1.5 ton 220V', 'MAGNUM 22 INV - 1.5 ton 220V'),  
    ('MAGNUM 22 INV - 2 ton 220V', 'MAGNUM 22 INV - 2 ton 220V'), 
    ('NEX - 1 ton 110V', 'NEX - 1 ton 110V'),  
    ('NEX - 1 ton 220V', 'NEX - 1 ton 220V'),  
    ('NEX - 1.5 ton 220V', 'NEX - 1.5 ton 220V'),  
    ('NEX - 2 ton 220V', 'NEX - 2 ton 220V'),  
    ('V32 INVERTER - 1 ton 110V', 'V32 INVERTER - 1 ton 110V'),  
    ('V32 INVERTER - 1 ton 220V', 'V32 INVERTER - 1 ton 220V'),  
    ('V32 INVERTER - 1.5 ton 220V', 'V32 INVERTER - 1.5 ton 220V'),  
    ('V32 INVERTER - 2 ton 220V', 'V32 INVERTER - 2 ton 220V'),
    ('XLIFE - 1 ton 110V', 'XLIFE - 1 ton 110V'),  
    ('XLIFE - 1 ton 220V', 'XLIFE - 1 ton 220V'),  
    ('XLIFE - 1.5 ton 220V', 'XLIFE - 1.5 ton 220V'),  
    ('XLIFE - 2 ton 220V', 'XLIFE - 2 ton 220V'),
    ('X32 INVERTER - 1 ton 110V', 'X32 INVERTER - 1 ton 110V'),  
    ('X32 INVERTER - 1 ton 220V', 'X32 INVERTER - 1 ton 220V'),  
    ('X32 INVERTER - 1.5 ton 220V', 'X32 INVERTER - 1.5 ton 220V'),
    ('X32 INVERTER - 2 ton 220V', 'X32 INVERTER - 2 ton 220V'), 
    ('X-ONE - 1 ton 110V', 'X-ONE - 1 ton 110V')
)

FORMA_PAGO =(
    ('Transferencia Electrónica','Transferencia Electrónica'),
    ('Efectivo','Efectivo'),
    ('Cheque Nominativo','Cheque Nominativo'),
    ('Por definir','Por definir'),
    ('Equipo','Equipo'),
)

METODO_PAGO =(
    ('Contado','Contado'),
    ('Crédito','Crédito'),
    ('Préstamo','Préstamo'),
)

FACTURACION =(
    ('Cliente', 'Cliente'),
    ('Empresa','Empresa'),
    ('Público en General', 'Publico en General'),
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
    precio_gral = models.PositiveIntegerField()
    precio_tec = models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural = 'Adquisición de Equipo'
        
    @property
    def precio_d1(self):
        return round(self.precio_tec * Decimal(1-0.03))
    
    @property
    def precio_d2(self):
        return round(self.precio_tec * Decimal(1-0.05))
    
    @property
    def precio_d3(self):
        return round(self.precio_tec * Decimal(1-0.08))
    
    def __str__(self):
        return f'{self.equipo}--{self.cantidad} Disponibles.'

class Datos_Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    forma_pago = models.CharField(max_length=100, choices=FORMA_PAGO)
    metodo_pago = models.CharField(max_length=100, choices=METODO_PAGO)
    tipo_factura = models.CharField(max_length=100, choices=FACTURACION)
    id = models.AutoField(primary_key=True)
    
    FORMA_PAGO_CONTADO = (
        ('Transferencia Electrónica','Transferencia Electrónica'),
        ('Efectivo', 'Efectivo'),
        ('Cheque Nominativo', 'Cheque Nominativo'),
        ('Equipo', 'Equipo'),
    )

    FORMA_PAGO_CREDITO = (
        ('Por definir', 'Por definir'),
    )
    
    FORMA_PAGO_PRESTAMO = (
        ('Equipo', 'Equipo'),
    )
    
    class Meta:
        verbose_name_plural = 'Orden de compra'
    
    def __str__(self):
        return f'{self.cliente} - Orden:{self.id}'

    def limit_choices_to(self):
        if self.metodo_pago == 'Contado':
            return {'forma_pago__in': [option[0] for option in self.FORMA_PAGO_CONTADO]}
        elif self.metodo_pago == 'Crédito':
            return {'forma_pago__in': [option[0] for option in self.FORMA_PAGO_CREDITO]}
        elif self.metodo_pago == 'Préstamo':
            return {'forma_pago__in': [option[0] for option in self.FORMA_PAGO_PRESTAMO]}
        else:
            return {}

class Equipos_Venta(models.Model):
    datos_venta = models.ForeignKey(Datos_Venta, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Pos_Equipo, on_delete=models.CASCADE)
    cantidad_equipos = models.PositiveBigIntegerField()
    
    class Meta:
        verbose_name_plural = 'Equipos solicitados'
    
    def __str__(self):
        return f'Entregar: {self.cantidad_equipos} {self.equipo.equipo} a {self.datos_venta.cliente}. FOLIO: {self.datos_venta.id}'