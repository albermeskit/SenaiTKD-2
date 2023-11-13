# Generated by Django 4.2.5 on 2023-10-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.PositiveIntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cidade', models.CharField(max_length=100)),
                ('faixa', models.CharField(choices=[('Branca', 'Branca'), ('Amarela', 'Amarela'), ('Verde', 'Verde'), ('Azul', 'Azul'), ('Vermelha', 'Vermelha'), ('Preta', 'Preta')], max_length=10)),
            ],
        ),
    ]
