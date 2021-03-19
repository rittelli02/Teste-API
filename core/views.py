from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Projeto, Gerenciamento
from .serealizers import UserSerializer, ProjSerializer, GerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET', 'POST'])
def Validate(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.valorGasto==0:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)