from django import forms
from . models import Producto, Order, Customer
from django.forms import ValidationError

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
    product_code = forms.CharField(label='Código del Producto')

    class Meta:
        model = Order
        fields = ['product_code', 'order_quantity', 'customer']
        labels = {
            'order_quantity': 'Cantidad',
            'customer': 'Cliente',
        }

    def clean_product_code(self):
        product_code = self.cleaned_data['product_code']
        products = Producto.objects.filter(code=product_code)

        if not products.exists():
            raise ValidationError('Producto no encontrado con el código proporcionado')
        elif products.count() > 1:
            raise ValidationError('Múltiples productos encontrados con el código proporcionado')
        
        return products.first()

    def save(self, commit=True):
        self.instance.product = self.cleaned_data['product_code']
        return super().save(commit)