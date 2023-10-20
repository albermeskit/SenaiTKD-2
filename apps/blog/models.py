from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=200)
    conteudo_noticia = RichTextUploadingField(config_name='default')

    def __str__(self):
        return self.titulo_noticia
