from django.urls import path
from .views import finalizar_prestamo, eliminar_prestamo, lista_prestamos
from .views import InicioView, lista_prestamos, editar_prestamo, agregar_prestamo, ver_prestamo

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('finalizar_prestamo/<int:id_prestamo>/', finalizar_prestamo, name='finalizar_prestamo'),
    path('eliminar_prestamo/<int:id_prestamo>/', eliminar_prestamo, name='eliminar_prestamo'),
    path('lista_prestamos/', lista_prestamos, name='lista_prestamos'),
    path('agregar_prestamo/', agregar_prestamo, name='agregar_prestamo'),
    path('editar_prestamo/<int:id_prestamo>/', editar_prestamo, name='editar_prestamo'),
    path('ver_prestamo/<int:id_prestamo>/', ver_prestamo, name='ver_prestamo'),
]
