from django.test import TestCase
from ..models import Categoria
from mixer.backend.django import mixer

class TestCategoriaModels(TestCase):
    def test_model_name_and_slug(self):
        mixer.blend(Categoria, id=1, nome='skate')
        categoria = Categoria.objects.first()

        self.assertEqual(categoria.id, 1)
        self.assertEqual(categoria.nome, "skate")
        self.assertEqual(categoria.slug, "skate")
  
