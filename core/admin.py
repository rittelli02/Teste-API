from django.contrib import admin
from .models import Usuario, Projeto, Gerenciamento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Projeto)
admin.site.register(Gerenciamento)