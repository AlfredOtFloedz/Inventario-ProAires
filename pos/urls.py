from django.urls import path
from . import views
from inventario import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista_clientes/', views.customer , name='pos-customer'),
    path('punto_venta/', views.pos_index , name='pos-index'),
    path('info_cliente/<int:pk>/', views.customer_detail , name='pos-customer-info'),
    path('registro_ventas/', views.pos_corte , name='pos-corte'),
]
# Agrega configuración para archivos estáticos y multimedia solo en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
