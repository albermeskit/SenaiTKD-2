from django.db import models
from apps.atletas.models import Atleta
# Create your models here.
class Fight(models.Model):
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

    atleta1 = models.ForeignKey(Atleta, related_name='fights_atleta1', on_delete=models.CASCADE)
    atleta2 = models.ForeignKey(Atleta, related_name='fights_atleta2', on_delete=models.CASCADE)
    data = models.DateField()
    faixa_atleta1= models.CharField(max_length=50,choices=FAIXA_CHOICES)
    faixa_atleta2= models.CharField(max_length=50,choices=FAIXA_CHOICES)
    local = models.CharField(max_length=100)
    valor_inscricao = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Competição  {self.atleta1} contra {self.atleta2} em {self.local} em {self.data}"






