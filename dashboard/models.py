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

YN = (
    ('yes', 'Si'),
    ('no', 'No'),
)

PAYMENT = (
    ('cash', 'Efectivo'),
    ('card', 'Tarjeta'),
    ('transaction','Tranferencia'),
)

TYPE = (
    ('SETCWC361B', 'SETCWC361B'),
    ('SETCWC261E', 'SETCWC261E'),
    ('SETCWC181E', 'SETCWC181E'),
    ('SETCWC121E', 'SETCWC121E'),
    ('SETCWC120E', 'SETCWC120E'),
    ('SETCMC261V', 'SETCMC261V'),
    ('SETCMC181V', 'SETCMC181V'),
    ('SETCMC121V', 'SETCMC121V'),
    ('SETCMC120V', 'SETCMC120V'),
    ('SETCLC261T', 'SETCLC261T'),
    ('SETCLC181T', 'SETCLC181T'),
    ('SETCLC121T', 'SETCLC121T'),
    ('SETCLC120T', 'SETCLC120T'),
    ('MBF16AF', 'MBF16AF'),
    ('MBF10BB', 'MBF10BB'),
    ('MBF06ZB', 'MBF06ZB'),
    ('MDD10CB', 'MDD10CB'),
    ('MDD10CS', 'MDD10CS'),    
)

class Precios(models.Model):
    precio_mirage = models.PositiveIntegerField(default=None)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
   
    @property
    def precio_compra(self):
        return self.precio_mirage * 0.95 * 1.16
    
    def precio_gral(self):
        return self.precio_compra * 2

    @property
    def precio_d0(self):
        return self.precio_compra * 1.5

    @property
    def precio_d1(self):
        return self.precio_d0 * 0.97

    @property
    def precio_d2(self):
        return self.precio_d0 * 0.95
    
    @property
    def precio_d3(self):
        return self.precio_d0 * 0.92
    
    class Meta:
        verbose_name_plural = 'Precios'
        
    def __str__(self):
        return f'{self.name}'

class Producto(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, blank=True)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    type = models.CharField(max_length=100, default=None, choices=TYPE, blank=True)
    precio = models.DecimalField(max_digits=20, decimal_places=2, default=10000.00, blank=True)
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

class Apartados(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE)
    order_quantity = models.PositiveBigIntegerField()
    pickup_date = models.DateTimeField(blank = True)
    payment = models.CharField(max_length=5, choices=YN)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Apartados'
    
    def __str__(self):
        return f'{self.product} pedido realizado por {self.staff.username}'
