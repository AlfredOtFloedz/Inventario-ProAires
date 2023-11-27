from django import forms
from . models import Customer

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