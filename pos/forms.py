from django import forms
from . models import Customer, Pos_Equipo
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
        fields = ['equipo', 'cantidad', 'precio_u', 'descuento']
        
        labels = {
            'equipo': 'Equipo',
            'cantidad': 'Cantidad recibida',
            'precio_u': 'Precio Neto',
            'descuento': 'Descuento Mirage',
        }

