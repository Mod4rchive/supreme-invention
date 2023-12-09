from django.contrib import admin
from .models import Participante, Tutor, Tutor_IA, Curso, Documento

# Register your models here.
admin.site.register(Participante)
admin.site.register(Tutor)
admin.site.register(Tutor_IA)
admin.site.register(Curso)
admin.site.register(Documento)