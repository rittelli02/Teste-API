from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Projeto, Gerenciamento
from .serealizers import UserSerializer, ProjSerializer, GerSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class ProjViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjSerializer

class GerViewSet(viewsets.ModelViewSet):
    queryset = Gerenciamento.objects.all()
    serializer_class = GerSerializer        