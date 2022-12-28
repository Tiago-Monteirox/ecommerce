from django.test import TestCase
from categoria.models import Categoria
from ..models import Produto
from mixer.backend.django import mixer

class TestProdutoModels(TestCase):
    def test_model_fields(self):
        mixer.blend(Categoria, id=100, nome='skate')
        mixer.blend(
            Produto,
            id=100,
            nome='skate',
            categoria_id=100,
            descricao_curta='teste',
            descricao_longa='teste1',
            preco_marketing=10.0,
            preco_marketing_promocional=9.6,
            tipo="V",
        )
        produto = Produto.objects.first()

        self.assertEqual(produto.id, 100)
        self.assertEqual(produto.nome, "skate")
        self.assertEqual(produto.slug, "skate")
        self.assertEqual(produto.categoria_id, 100)
        self.assertEqual(produto.descricao_curta, "teste")
        self.assertEqual(produto.descricao_longa, "teste1")
        self.assertEqual(produto.preco_marketing, 10.0)
        self.assertEqual(produto.preco_marketing_promocional, 9.6)
        self.assertEqual(produto.tipo, "V")
  
