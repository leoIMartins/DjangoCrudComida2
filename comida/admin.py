from django.contrib import admin
from .models import Comida, Tipo, Opcoes, Salada

# Register your models here.
admin.site.register(Comida)
admin.site.register(Tipo)
admin.site.register(Opcoes)
admin.site.register(Salada)
