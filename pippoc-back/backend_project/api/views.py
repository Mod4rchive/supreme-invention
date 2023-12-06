from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .models import Participante, Tutor_IA, Tutor, Curso, Documento
from .serializer import ParticipanteSerializer, Tutor_IASerializer, TutorSerializer, CursoSerializer, DocumentoSerializer
from rest_framework import viewsets



class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

class TutorIAViewSet(viewsets.ModelViewSet):
    queryset = Tutor_IA.objects.all()
    serializer_class = Tutor_IASerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

