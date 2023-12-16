from django.contrib import admin
from . models import Customer, CustomerID, Pos_Equipo, Datos_Venta, Equipos_Venta
# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerID)
admin.site.register(Pos_Equipo)
admin.site.register(Datos_Venta)
admin.site.register(Equipos_Venta)

