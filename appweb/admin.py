from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profesional)
admin.site.register(Contacto)
class AtencionAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Verificar si el usuario tiene permisos de visualización en el modelo
        if request.user.has_perm('appweb.view_atencion'):
            return True
        return False
admin.site.register(Atencion, AtencionAdmin)
admin.site.register(TrabajaConNosotros)
