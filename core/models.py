from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=80, null=False)
    email = models.EmailField(max_length=50,null=False)
    senha = models.CharField(max_length=30, null=False)
    perfil = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome


class Projeto(models.Model):
    codigoProj = models.CharField(max_length=20, null=False)
    nomeProj = models.EmailField(max_length=80,null=False)
    descProj = models.TextField(max_length=2000, null=False)
    dtCadastro = models.DateField(null=False)
    dtAprovacao = models.DateField(null=False)
    dtCancelamento = models.DateField(null=False)
    numUsu = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigoProj


class Gerenciamento(models.Model):
    numProj = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    valorOrcamento = models.DecimalField(max_digits=9, decimal_places=2)
    valorGasto = models.DecimalField(max_digits = 9,decimal_places = 2) 
    
    def __str__(self):
        return self.numProj



