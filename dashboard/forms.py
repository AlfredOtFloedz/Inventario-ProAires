from django import forms
from . models import Producto, Order, Customer

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['code', 'name', 'category', 'type', 'quantity', 'precio']    
        labels = {
        'code': 'Código',
        'name': 'Nombre',
        'category': 'Categoría',
        'type': 'Modelo',
        'quantity': 'Cantidad',
        'precio': 'Precio',
        }
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity', 'customer']
        labels = {
        'product': 'Producto',
        'order_quantity': 'Cantidad',
        'customer': 'Cliente',
        }