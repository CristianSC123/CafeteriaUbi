from django.contrib import admin

from apps.Clientes.models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","email","correo","avatar")