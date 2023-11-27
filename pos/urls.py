from django.urls import path
from . import views

urlpatterns = [
    path('lista_clientes/', views.customer , name='pos-customer'),
    path('facturacion/', views.pos_facturacion , name='pos-facturacion'),
    path('punto_venta/', views.pos_index , name='pos-index'),
    path('registro_clientes/', views.new_customer , name='dashboard-new-customer'),
]
