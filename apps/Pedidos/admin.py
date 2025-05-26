from django.contrib import admin
from .models import Pedido
# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'id_cliente', 'id_producto', 'cantidad', 'fecha_pedido', 'fecha_entrega', 'estado')
    