# Generated by Django 4.2.5 on 2023-10-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fight', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fight',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='fight',
            name='faixa_categoria',
        ),
        migrations.AddField(
            model_name='fight',
            name='faixa_atleta1',
            field=models.CharField(choices=[('Branca', 'Branca'), ('Amarela', 'Amarela'), ('Amarela', 'Amarela-Verde'), ('Verde', 'Verde'), ('Verde', 'Verde-Azul'), ('Azul', 'Azul'), ('Azul', 'Azul-Vermelha'), ('Vermelha', 'Vermelha'), ('Vermelha', 'Vermelha-Preta'), ('Preta', 'Preta 1 ao 9 DAN')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fight',
            name='faixa_atleta2',
            field=models.CharField(choices=[('Branca', 'Branca'), ('Amarela', 'Amarela'), ('Amarela', 'Amarela-Verde'), ('Verde', 'Verde'), ('Verde', 'Verde-Azul'), ('Azul', 'Azul'), ('Azul', 'Azul-Vermelha'), ('Vermelha', 'Vermelha'), ('Vermelha', 'Vermelha-Preta'), ('Preta', 'Preta 1 ao 9 DAN')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
