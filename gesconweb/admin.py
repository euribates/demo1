from django.contrib import admin

# Register your models here.

from gesconweb.models import Aplicativo

class AplicativoAdmin(admin.ModelAdmin):
     
    date_hierarchy = 'f_creacion'
    list_filter = ('activo', 'f_creacion',)
    list_display = ('id', 'nombre', 'slug', 'activo', 'email')
    search_fields = ('nombre', 'descripcion', 'slug',)
    prepopulated_fields = {
        'slug': ('nombre', ),
        }

admin.site.register(Aplicativo, AplicativoAdmin)

