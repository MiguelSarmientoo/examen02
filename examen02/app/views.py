from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Prestamo, Libro, Usuario, Autor
from django.http import HttpResponseNotFound

from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = 'inicio.html'

def lista_prestamos(request):
    prestamos = Prestamo.objects.filter(finalizado=False)
    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()

    return render(request, 'lista_prestamos.html', {'prestamos': prestamos, 'libros': libros, 'usuarios': usuarios})

def editar_prestamo(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)

    if request.method == 'POST':
        libro_id = request.POST.get('libro')
        usuario_id = request.POST.get('usuario')
        fecha_prestamo = request.POST.get('fecha_prestamo')
        fecha_devolucion = request.POST.get('fecha_devolucion')

        libro = get_object_or_404(Libro, pk=libro_id)
        usuario = get_object_or_404(Usuario, pk=usuario_id)

        prestamo.libro = libro
        prestamo.usuario = usuario
        prestamo.fecha_prestamo = fecha_prestamo
        prestamo.fecha_devolucion = fecha_devolucion
        prestamo.finalizado = False  

        prestamo.save()

        return redirect('lista_prestamos')

    libros = Libro.objects.all()
    usuarios = Usuario.objects.all()
    autores = Autor.objects.all()  

    return render(request, 'editar_prestamo.html', {'prestamo': prestamo, 'libros': libros, 'usuarios': usuarios, 'autores': autores})


def agregar_prestamo(request):
    if request.method == 'POST':
        try:
            libro_id = request.POST.get('libro')
            libro = Libro.objects.get(pk=libro_id)
            
            autor_id = request.POST.get('autor')
            autor = Autor.objects.get(pk=autor_id)

            usuario_id = request.POST.get('usuario')
            usuario = Usuario.objects.get(pk=usuario_id)

            fecha_prestamo = request.POST.get('fecha_prestamo')
            fecha_devolucion = request.POST.get('fecha_devolucion')

            Prestamo.objects.create(
                libro=libro,
                autor=autor,
                usuario=usuario,
                fecha_prestamo=fecha_prestamo,
                fecha_devolucion=fecha_devolucion,
                finalizado=False
            )

            return redirect('lista_prestamos')

        except Libro.DoesNotExist or Autor.DoesNotExist or Usuario.DoesNotExist:
            return HttpResponseNotFound("El libro, autor o usuario seleccionado no existe.")

    libros = Libro.objects.all()
    autores = Autor.objects.all()
    usuarios = Usuario.objects.all()

    return render(request, 'agregar_prestamo.html', {'libros': libros, 'autores': autores, 
                                                     'usuarios': usuarios})

def eliminar_prestamo(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)
    prestamo.delete()
    return redirect('lista_prestamos')

def finalizar_prestamo(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)

    if not prestamo.finalizado:
        prestamo.fecha_devolucion = timezone.now()
        prestamo.finalizado = True
        prestamo.save()

    return redirect('lista_prestamos')

def ver_prestamo(request, id_prestamo):
    prestamo = get_object_or_404(Prestamo, id_prestamo=id_prestamo)
    autores = Autor.objects.all() 
    return render(request, 'ver_prestamo.html', {'prestamo': prestamo, 'autores': autores})
