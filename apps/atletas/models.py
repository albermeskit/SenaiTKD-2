from django.db import models

class Atleta(models.Model):
    FAIXA_CHOICES = (
        ('Branca', 'Branca'),
        ('Amarela', 'Amarela'),
        ('Amarela', 'Amarela-Verde'),
        ('Verde', 'Verde'),
        ('Verde', 'Verde-Azul'),
        ('Azul', 'Azul'),
        ('Azul', 'Azul-Vermelha'),
        ('Vermelha', 'Vermelha'),
        ('Vermelha', 'Vermelha-Preta'),
        ('Preta', 'Preta 1 ao 9 DAN'),
    )

    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    cidade = models.CharField(max_length=100)
    faixa = models.CharField(max_length=10, choices=FAIXA_CHOICES)

    def __str__(self):
        return self.nome

























