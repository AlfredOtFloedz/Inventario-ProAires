from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.db.models import Sum
from django.http import HttpResponse
from datetime import timezone

from . models import Customer
from dashboard.models import Producto, Order
from . forms import CustomerForm
from dashboard.forms import ProductoForm, OrderForm

#Credenciales
import barcode
from barcode.writer import ImageWriter

# Create your views here.
@login_required
def pos_index(request):
    orders = Order.objects.all()
    productos = Producto.objects.all()
    total_quantity = productos.aggregate(Sum('quantity'))['quantity__sum']
    workers_count = User.objects.count()
    items_count = Producto.objects.count()
    orders_count = orders.count()
    total_order_quantity = orders.aggregate(Sum('order_quantity'))['order_quantity__sum']
    customer_count = Customer.objects.count()

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

                return redirect('pos-index')
            
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
        'customer_count': customer_count
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
    customer_count = customer.count()
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
        'customer_count': customer_count,
    }
    return render(request, 'pos/customers_list.html', context)

@login_required
def customer_detail(request, pk):
    customers = Customer.objects.get(id=pk)
    customer_count = Customer.objects.count()
    
    context = {
        'customers':customers,
        'customer_count': customer_count,
    }
    return render(request, 'pos/customer_detail.html', context)

@login_required
def pos_facturacion(request):
    items = Producto.objects.all()
    items_count = items.count()
    total_quantity = items.aggregate(Sum('quantity'))['quantity__sum']
    workers_count = User.objects.count()
    orders_count = Order.objects.count()
    total_order_quantity = Order.objects.aggregate(Sum('order_quantity'))['order_quantity__sum']
    customer_count = Customer.objects.count()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            producto_name = form.cleaned_data.get('name')
            messages.success(request, f'{producto_name} se ha añadido correctamente')
            return redirect('pos-facturacion')
    else: 
        form = ProductoForm()
        
    context = {
        'items': items,
        'form' : form,
        'workers_count': workers_count,
        'items_count': items_count,
        'orders_count': orders_count,
        'total_quantity': total_quantity,
        'total_order_quantity':total_order_quantity ,
        'customer_count':customer_count,

    } 
    return render(request, 'pos/factura.html', context)
    