from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('flor', FlorViewSet)

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario2,name='FORMU'),
    path('quienes_somos/',quienes_somos,name='QUIEN'),  
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('login/',login,name='LOGIN'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR_SESION'),
    path('login_iniciar/',login_iniciar,name='LOGIN_INICIAR'),
    path('agregar_carro/<id>/',agregar_carro,name='AGREGAR_CARRO'),
    path('carrito/',carrito,name='CARRITO'),
    path('vaciar_carrito/',vacio_carrito,name='VACIARCARRITO'),
    path('registro/',registro_usuario,name='REGISTRO'),
    path('guardar-token/', guardar_token,name='guardar_token'),
    path('api/',include(router.urls)),
]