from django import forms
from . models import Customer, Pos_Equipo, Datos_Venta, Equipos_Venta
from dashboard.models import Producto

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [ 'customer_name', 'status', 'RFC', 'DIR', 'CFDI', 'REG_FIS', 'c_email', 'c_phone', 'image']

        labels = {
        'customer_name': 'Nombre del Cliente',
        'status': 'Categoría',
        'RFC': 'RFC',
        'DIR': 'Dirección',
        'CFDI': 'CFDI',
        'REG_FIS': 'Régimen Fiscal',
        'c_phone': 'Teléfono',
        'c_email' : 'Correo Elctrónico',
        'image': 'Foto'
        }

class Compra_EquiposForm(forms.ModelForm):
    
    class Meta:
        model = Pos_Equipo
        fields = ['equipo', 'cantidad', 'precio_gral','precio_tec']

        labels = {
            'equipo': 'Equipo',
            'cantidad': 'Existencias',
            'precio_gral': 'Precio A Público En General',
            'precio_tec':'Precio Técnico',
        }

class Datos_VentaForm(forms.ModelForm):
    
    class Meta:
        model = Datos_Venta
        fields = ['cliente', 'metodo_pago', 'forma_pago', 'tipo_factura']
        
        labels = {
            'cliente': 'Cliente',
            'forma_pago': 'Forma de Pago',
            'metodo_pago': 'Método de Pago',
            'tipo_factura': 'Facturar a:'
        }

class Equipos_VentaForm(forms.ModelForm):
    
    class Meta:
        model = Equipos_Venta
        fields = ['datos_venta', 'equipo', 'cantidad_equipos']

