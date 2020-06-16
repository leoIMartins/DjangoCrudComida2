from django.db import models


class Tipo(models.Model):
    descricao = models.CharField(max_length=100)
    origem = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao


class Opcoes(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Salada(models.Model):
    descricao = models.CharField(max_length=100)
    dtColheita = models.CharField(max_length=10)

    def __str__(self):
        return self.descricao


class Comida(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    descricao = models.CharField(max_length=50)
    quantidade = models.PositiveIntegerField()
    opcoes = models.ForeignKey(Opcoes, on_delete=models.SET_NULL, null=True)
    valorCalorico = models.PositiveIntegerField()
    salada = models.ForeignKey(Salada, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.tipoComida
