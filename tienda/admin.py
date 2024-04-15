from django.contrib import admin
from .models import Categoria, Producto, Cliente

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'fecha_nacimiento', 'fecha_publicacion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    actions = ['actualizar_stock_a_20']

    def actualizar_stock_a_20(self, request, queryset):
        queryset.update(stock=20)

    actualizar_stock_a_20.short_description = "Actualizar Stock a 20 unidades"

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
