from django.contrib import admin
from .models import Libro, Autor, Usuario, Prestamo

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id_prestamo', 'libro', 'autor', 'usuario', 'fecha_prestamo', 'fecha_devolucion', 'finalizado_display')

    def libro_display(self, obj):
        return str(obj.libro)

    libro_display.short_description = 'Libro'

    def finalizado_display(self, obj):
        return obj.finalizado

    finalizado_display.short_description = 'Finalizado'

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Usuario)
admin.site.register(Prestamo, PrestamoAdmin)
