from django.urls import path
from categoria import views

app_name = "categoria"

urlpatterns = [
    path('criar/', views.CriarCategoria.as_view(), name="criar"),
    path('lista/', views.ListaCategoria.as_view(), name="lista"),
    # path('criarsubcategoria/', views.CriarSubCategoria.as_view(), name="criar_subcategoria"),
]


