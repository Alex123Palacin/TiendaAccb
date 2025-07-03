
#alex
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import ClienteViewSet, ClienteLoginAPIView
from productos.views import ProductoViewSet
from carritos.views import CarritoViewSet
from detallecarro.views import DetalleCarroViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'carritos', CarritoViewSet)
router.register(r'detallecarro', DetalleCarroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Agregamos el endpoint de login de clientes:
    path('api/clientes/login/', ClienteLoginAPIView.as_view(), name='cliente-login'),
    path('api/', include(router.urls)),
]



