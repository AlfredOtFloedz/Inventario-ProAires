from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.db.models import Sum
from django.http import HttpResponse
from datetime import timezone
from django.db.models import F


from . models import Customer, CustomerID, Pos_Equipo, Datos_Venta, Equipos_Venta
from dashboard.models import Producto, Order
from . forms import CustomerForm, Compra_EquiposForm, Datos_VentaForm, Equipos_VentaForm
from dashboard.forms import ProductoForm, OrderForm

# Create your views here.
@login_required
def pos_index(request):
    equipos = Pos_Equipo.objects.all
    datos_venta = Datos_Venta.objects.all()
    equipos_venta = Equipos_Venta.objects.all()
    total_equipos_venta = equipos_venta.aggregate(Sum('cantidad_equipos'))['cantidad_equipos__sum']
    total_ventas = datos_venta.count()

    if request.method == 'POST':
        form = Datos_VentaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nombre_cliente = form.cleaned_data.get('cliente')
            messages.success(request, f'Se ha añadido una orden de venta para {nombre_cliente}')
            return redirect('pos-index')
    else: 
        form = Datos_VentaForm()
            
    context = {
        'form': form,
        'equipos':equipos,
        'datos_venta':datos_venta,
        'equipos_venta':equipos_venta,
        'total_equipos_venta':total_equipos_venta,
        'total_ventas':total_ventas,
    }
    return render(request, 'pos/pos_index.html', context)

@login_required
def pos_equipos_venta(request):
    equipos = Pos_Equipo.objects.all
    datos_venta = Datos_Venta.objects.all()
    equipos_venta = Equipos_Venta.objects.all()
    total_equipos_venta = equipos_venta.aggregate(Sum('cantidad_equipos'))['cantidad_equipos__sum']
    total_ventas = datos_venta.count()

    if request.method=='POST':
        form = Equipos_VentaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            
            if instance.cantidad_equipos <= instance.equipos.cantidad:
                instance.equipo.cantidad -= instance.cantidad_equipos
                instance.equipo.save()
                instance.save()
                messages.success(request, '¡Pedido añadido exitosamente!')

                return redirect('pos-index')
            
            else: 
                form.add_error('cantidad_equipos', f'Solo hay {instance.equipos.cantidad} en existencia.')    
            
    else:
        form = Equipos_VentaForm()
    context = {
        'form': form,
        'equipos':equipos,
        'datos_venta':datos_venta,
        'equipos_venta':equipos_venta,
        'total_equipos_venta':total_equipos_venta,
        'total_ventas':total_ventas,
    }
    return render(request, 'pos/pos_index.html', context)

@login_required
def customer(request):
    orders = Order.objects.all()
    productos = Producto.objects.all()
    total_quantity = productos.aggregate(Sum('quantity'))['quantity__sum']
    workers_count = User.objects.count()
    items_count = Producto.objects.count()
    orders_count = orders.count()
    total_order_quantity = orders.aggregate(Sum('order_quantity'))['order_quantity__sum']
    customer = Customer.objects.all()
        
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data.get('customer_name')
            messages.success(request, f'{customer_name} se ha añadido correctamente')
            return redirect('pos-customer')
    else: 
        form = CustomerForm()
    context = {
        'orders':orders,
        'form': form,
        'productos':productos,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_order_quantity':total_order_quantity,
        'total_quantity': total_quantity,
        'customer': customer,
    }
    return render(request, 'pos/customers_list.html', context)

@login_required
def customer_detail(request, pk):
    customers = Customer.objects.get(id=pk)
    barcode = CustomerID.objects.filter(customer=customers).first()   
     
    context = {
        'customers':customers,
        'barcode':barcode,
    }
    return render(request, 'pos/customer_detail.html', context)

@login_required
def registro_equipos(request):
    equipos = Pos_Equipo.objects.values('equipo').annotate(total_quantity=Sum('cantidad'))
    
    if request.method == 'POST':
        form = Compra_EquiposForm(request.POST)
        if form.is_valid():
            form.save()
            
            equipo_cantidad = form.cleaned_data.get('cantidad')
            equipo_nombre = form.cleaned_data.get('equipo')
            messages.success(request, f'Se han añadido {equipo_cantidad} equipos {equipo_nombre} correctamente')
            return redirect('pos-adquisicion-equipos')
    else: 
        form = Compra_EquiposForm()    

    context = {
        'form':form,
        'equipos':equipos,
    }
    return render(request, 'pos/equipos_compra.html', context)

@login_required
def precio_equipos(request):
    # Selecciona solo una entrada por cada valor único en el campo "equipo"
    productos = Pos_Equipo.objects.all().order_by('equipo')
    
    context = {
        'productos': productos,
    }
    return render(request, 'pos/precio.html', context)

@login_required
def pos_corte(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    total_order_quantity = orders.aggregate(Sum('order_quantity'))['order_quantity__sum']
    customer_count = Customer.objects.count()

    context = {
        'orders': orders, 
        'orders_count': orders_count,
        'total_order_quantity':total_order_quantity ,
        'customer_count': customer_count,
    }
    return render(request, 'pos/pos_corte.html', context)

def equipo_actualizar(request, pk):
    equipo = Pos_Equipo.objects.get(id=pk)

    if request.method == "POST":
        equipo_form = Compra_EquiposForm(request.POST, instance=equipo)
        if equipo_form.is_valid():
            equipo_form.save()
            return redirect('pos-precio-equipos')
    else:
        equipo_form = Compra_EquiposForm(instance=equipo)

    context = {
        'equipo_form': equipo_form,
    }
    
    return render(request, 'pos/actualizar_equipo.html', context)