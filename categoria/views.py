from django.shortcuts import render, get_object_or_404, reverse
from produto import views, models
from .models import Categoria, SubCategoria
from produto.models import Produto
from django.views.generic.edit import CreateView

def lista_produto(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()

class CriarCategoria(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'categoria/criar.html'

    def get_success_url(self):
        return reverse("produto:lista")

class CriarSubCategoria(CreateView):
    model = SubCategoria
    fields = '__all__'
    template_name = 'categoria/criar_subcategoria.html'

    def get_success_url(self):
        return reverse("produto:lista")