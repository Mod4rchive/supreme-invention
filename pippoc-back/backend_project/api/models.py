from django.db import models

# Create your models here.

class Participante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)

class Tutor_IA(models.Model):
    nombre = models.CharField(max_length=30)


class Tutor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    especialidades = models.CharField(max_length=30)

class Curso(models.Model):
    descripcion = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)


class Documento(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=30)
    formato = models.CharField(max_length=30)
