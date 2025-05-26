from django.contrib import admin
from .models import Ventas,DetalleVenta

class DetalleVentaTabular(admin.TabularInline):  
    extra = 1

@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    list_display = ("fecha_venta", "total", "cliente")
    inlines = [DetalleVentaTabular]  

    

# Register your models here.
