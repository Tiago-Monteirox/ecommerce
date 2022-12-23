from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    subcategoria = models.ForeignKey('SubCategoria', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('', args=[self.slug])


class SubCategoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'subcategoria'
        verbose_name_plural = 'subcategorias'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('', args=[self.slug])
    