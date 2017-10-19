from django.contrib import admin

# Register your models here.

from gesconweb.models import Aplicativo, Permiso

class AplicativoAdmin(admin.ModelAdmin):
     
    date_hierarchy = 'f_creacion'
    list_filter = ('activo', 'f_creacion',)
    list_display = ('id', 'nombre', 'slug', 'activo', 'email')
    search_fields = ('nombre', 'descripcion', 'slug',)
    prepopulated_fields = {
        'slug': ('nombre', ),
        }

class PermisoAdmin(admin.ModelAdmin):
     pass

admin.site.register(Permiso, PermisoAdmin)
admin.site.register(Aplicativo, AplicativoAdmin)
