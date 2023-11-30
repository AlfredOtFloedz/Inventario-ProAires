from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from datetime import timezone

from . models import Producto, Order, Precios
from . forms import ProductoForm, OrderForm
from pos.models import Customer
import csv
from django.db.models import Sum

# Create your views here.

@login_required
#@login_required(login_url='user-login') #Fuerza a iniciar sesión antes de mostrar la página
def index(request):
    orders = Order.objects.all()
    productos = Producto.objects.all()
    total_quantity = productos.aggregate(Sum('quantity'))['quantity__sum']
    workers_count = User.objects.count()
    items_count = Producto.objects.count()
    orders_count = orders.count()
    total_order_quantity = orders.aggregate(Sum('order_quantity'))['order_quantity__sum']

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            
            if instance.order_quantity <= instance.product.quantity:
                instance.product.quantity -= instance.order_quantity
                instance.product.save()
                instance.save()
                messages.success(request, '¡Pedido añadido exitosamente!')

                return redirect('dashboard-index')
            
            else: 
                form.add_error('order_quantity', f'Solo hay {instance.product.quantity} en existencia.')    
            
    else:
        form = OrderForm()
    context = {
        'orders':orders,
        'form':form,
        'productos':productos,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_order_quantity':total_order_quantity,
        'total_quantity': total_quantity,
    }
    return render(request, 'dashboard/index.html', context)

@login_required #En este caso el comando es más corto porque se ha especificado en /inventario/settings.py el url por defecto
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    items_count = Producto.objects.count()
    total_quantity = Producto.objects.aggregate(Sum('quantity'))['quantity__sum']
    orders_count = Order.objects.count()
    total_order_quantity = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum']

    context = {
        'workers':workers,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_quantity': total_quantity,
        'total_order_quantity':total_order_quantity ,


    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    items_count = Producto.objects.count()
    total_quantity = Producto.objects.aggregate(Sum('quantity'))['quantity__sum']
    orders_count = Order.objects.count()
    total_order_quantity = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum']
    workers = User.objects.get(id=pk)
    workers_count = User.objects.count()
    
    context = {
        'workers':workers,
        'items_count': items_count,
        'total_quantity': total_quantity,
        'orders_count': orders_count,
        'total_order_quantity': total_order_quantity,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/staff_detail.html', context)

def assign_model_from_code(code):
    # Definir las concordancias entre códigos y modelos
    code_model_mapping = {
        'CWC361B': 'SETCWC361B',
        'CWC261E': 'SETCWC261E',
        'CWC181E': 'SETCWC181E',
        'CWC121E': 'SETCWC121E',
        'CWC120E': 'SETCWC120E',
        'CMC261V': 'SETCMC261V',
        'CMC181V': 'SETCMC181V',
        'CMC121V': 'SETCMC121V',
        'CMC120V': 'SETCMC120V',
        'CLC261T': 'SETCLC261T',
        'CLC181T': 'SETCLC181T',
        'CLC121T': 'SETCLC121T',
        'CLC120T': 'SETCLC120T',
        'EWC361B': 'SETCWC361B',
        'EWC261E': 'SETCWC261E',
        'EWC181E': 'SETCWC181E',
        'EWC121E': 'SETCWC121E',
        'EWC120E': 'SETCWC120E',
        'EMC261V': 'SETCMC261V',
        'EMC181V': 'SETCMC181V',
        'EMC121V': 'SETCMC121V',
        'EMC120V': 'SETCMC120V',
        'ELC261T': 'SETCLC261T',
        'ELC181T': 'SETCLC181T',
        'ELC121T': 'SETCLC121T',
        'ELC120T': 'SETCLC120T',
        'MBF16AF': 'MBF16AF',
        'MBF10BB': 'MBF10BB',
        'MBF06ZB': 'MBF06ZB',
        'MDD10CB': 'MDD10CB',
        'MDD10CS': 'MDD10CS', 
        # Agrega más concordancias según sea necesario
    }

    # Obtener las primeras tres letras del código
    code_prefix = code[:7]

    # Buscar el modelo correspondiente en el mapeo
    model = code_model_mapping.get(code_prefix, None)

    return model


@login_required
def producto(request):
    # Obtener la suma de cantidades por combinación única de nombre, modelo y categoría
    items = Producto.objects.values('name', 'type',).annotate(total_quantity=Sum('quantity'))
    items_count = Producto.objects.count()
    total_quantity = sum(item['total_quantity'] for item in items)
    workers_count = User.objects.count()
    orders_count = Order.objects.count()
    total_order_quantity = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum']

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Obtener el código ingresado en el formulario
            product_code = form.cleaned_data.get('code')

            # Asignar automáticamente el modelo basado en el código
            assigned_model = assign_model_from_code(product_code)
            
            # Asegurarse de que el modelo se haya asignado antes de guardar
            if assigned_model:
                form.instance.type = assigned_model
            else:
                # Si no se asigna automáticamente, asigna un valor predeterminado o maneja el error
                form.instance.type = 'DEFAULT_MODEL'

            form.save()
            producto_name = form.cleaned_data.get('name')
            messages.success(request, f'{producto_name} Se ha añadido correctamente')
            return redirect('dashboard-producto')

    else:
        form = ProductoForm()
        
    context = {
        'items': items,
        'form' : form,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_quantity': total_quantity,
        'total_order_quantity': total_order_quantity,
    } 
    return render(request, 'dashboard/producto.html', context)

@login_required
def producto_delete(request, pk):
    item = Producto.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('dashboard-registros')
    return render(request, 'dashboard/producto_delete.html')

@login_required
def producto_update(request, pk):
    item = Producto.objects.get(id=pk)

    if request.method == "POST":
        producto_form = ProductoForm(request.POST, instance=item)
        if producto_form.is_valid():
            # Guarda el valor antiguo de precio
            old_precio = item.precio

            # Actualiza el formulario
            producto_form.save()

            # Compara el precio actual con el precio antiguo
            if old_precio != item.precio:
                # Si el precio ha cambiado, actualiza updated_at
                print(f"Old: {old_precio}, New: {item.precio}")
                item.price_update = timezone.now()
                item.save()

            return redirect('dashboard-precio')
    else:
        producto_form = ProductoForm(instance=item)

    context = {
        'producto_form': producto_form,
    }

    return render(request, 'dashboard/producto_update.html', context)

@login_required
def producto_registro(request):
    items = Producto.objects.all().order_by('name')
    items_count = items.count()
    total_quantity = items.aggregate(Sum('quantity'))['quantity__sum']

    workers_count = User.objects.count()
    orders_count = Order.objects.count()
    total_order_quantity = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum']

    context = {
        'items': items,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_quantity': total_quantity,
        'total_order_quantity':total_order_quantity ,

    } 
    return render(request, 'dashboard/producto_registro.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    total_order_quantity = orders.aggregate(Sum('order_quantity'))['order_quantity__sum']

    workers_count = User.objects.count()
    items_count = Producto.objects.count()
    total_quantity = Producto.objects.aggregate(Sum('quantity'))['quantity__sum']

    context = {
        'orders': orders, 
        'orders_count': orders_count,
        'total_order_quantity':total_order_quantity ,
        'workers_count': workers_count,
        'items_count': items_count,
        'total_quantity': total_quantity,

    }
    return render(request, 'dashboard/order.html', context)

@login_required
#Generate Text File Venue List
def producto_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=productos.csv'
    
    #Crete a csv writer
    writer = csv.writer(response)
    
    #Model Designated
    items = Producto.objects.all()
    
    #Add column headings to the csv file 
    writer.writerow(['CODIGO', 'NOMBRE', 'CATEGORIA', 'PRECIO', 'CANTIDAD', 'ACTUALIZACION'],)
    
    for item in items: 
        writer.writerow([item.code, item.name, item.category, item.precio, item.quantity, item.updated_at])
    
    return response

@login_required
#Generate Text File Venue List
def order_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=pedidos.csv'
    
    #Crete a csv writer
    writer = csv.writer(response)
    
    #Model Designated
    orders = Order.objects.all()
    
    #Add column headings to the csv file 
    writer.writerow(['CODIGO', 'NOMBRE', 'CATEGORIA', 'CANTIDAD', 'STAFF', 'FECHA', 'CLIENTE',])
    
    for order in orders: 
        writer.writerow([order.product.code, order.product.name, order.product.category, order.order_quantity, order.staff, order.date, order.customer])
    
    return response

@login_required
def precio(request):
    productos = Precios.objects.all()
    
    context = {
        'productos': productos
    }
    return render(request, 'dashboard/precio.html', context)

