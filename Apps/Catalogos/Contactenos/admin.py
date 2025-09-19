from django.contrib import admin

from Apps.Catalogos.Contactenos.models import Contactos

@admin.register(Contactos)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Nombres', 'Apellidos','Email','Asunto', 'Mensaje','FechaCreacion']
    search_fields = ['Nombres', 'Apellidos', 'Email']