from django.db import models

class Position(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position

class Imovel(models.Model):
        tipo = models.CharField(max_length=100)
        area = models.CharField(max_length=100)
        endereco = models.CharField(max_length=100)
        cep = models.CharField(max_length=100)
        position = models.ForeignKey(Position, on_delete=models.CASCADE)
