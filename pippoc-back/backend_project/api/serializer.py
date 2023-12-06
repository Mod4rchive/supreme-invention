from django.db.models import fields
from rest_framework import serializers
from .models import Participante, Tutor_IA, Tutor, Curso, Documento

class ParticipanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'

class Tutor_IASerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor_IA
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

