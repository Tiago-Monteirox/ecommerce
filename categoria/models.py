from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import os
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    # subcategoria = models.ForeignKey('SubCategoria', on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('', args=[self.slug])

  
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)    
    
    def get_absolute_url(self):
        return reverse('', args=[self.slug])
    


# class SubCategoria(models.Model):
#     nome = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)