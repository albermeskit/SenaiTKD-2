# Generated by Django 4.2.6 on 2023-10-11 17:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='conteudo_noticia',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
