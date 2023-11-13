from django.shortcuts import render
from .models import Atleta
# Create your views here.
def atletas(request):
    atletas = Atleta.objects.all()

    dados = {
        "atletas": atletas
    }
    return render(request, "blog.html", dados)