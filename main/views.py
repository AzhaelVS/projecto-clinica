from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class UserViewSet (viewsets.ModelViewSet):
    model = UserCustom
    serializer_class = UserSerializer
    queryset = UserCustom.objects.all()

class MedicoViewSet (viewsets.ModelViewSet):
    model = Medico
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()

class PasienteViewSet (viewsets.ModelViewSet):
    model = Pasiente
    serializer_class = PasienteSerializer
    queryset = Pasiente.objects.all()

class AreaViewSet (viewsets.ModelViewSet):
    model = AreasMedicasabs
    serializer_class = AreaSerializer
    queryset = AreasMedicasabs.objects.all()

class RecetaViewSet (viewsets.ModelViewSet):
    model = Recetas
    serializer_class = RecetasSerializer
    queryset = Recetas.objects.all()
