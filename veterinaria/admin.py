from django.contrib import admin
from .models import Cliente, Mascota, Personal, Cita

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Personal)
admin.site.register(Cita)