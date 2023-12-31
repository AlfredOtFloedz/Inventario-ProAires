from django.urls import path
from . import views
from inventario import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista_clientes/', views.customer , name='pos-customer'),
    path('punto_venta/', views.pos_index , name='pos-index'),
    path('registro_adquisicion_equipos/', views.registro_equipos , name='pos-adquisicion-equipos'),
    path('registro_precio_equipos/', views.precio_equipos , name='pos-precio-equipos'),
    path('info_cliente/<int:pk>/', views.customer_detail , name='pos-customer-info'),
    path('registro_ventas/', views.pos_corte , name='pos-corte'),
    path('actualizar/equipo/<int:pk>/', views.equipo_actualizar, name='pos-equipo-actualizar'),
]
# Agrega configuración para archivos estáticos y multimedia solo en entorno de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)