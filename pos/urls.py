from django.urls import path
from . import views
from inventario import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista_clientes/', views.customer , name='pos-customer'),
    path('facturacion/', views.pos_facturacion , name='pos-facturacion'),
    path('punto_venta/', views.pos_index , name='pos-index'),
    path('info_cliente/<int:pk>/', views.customer_detail , name='pos-customer-info'),
    path('registro_clientes/', views.new_customer , name='dashboard-new-customer'),
]
# Agrega configuración para archivos estáticos y multimedia solo en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
