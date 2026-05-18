from django.contrib import admin
from .models import Autor, Categoria, Editora, Livro
# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao',)
    search_fields = ('nome',)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome','cidade','site',)
    search_fields = ('nome',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome','nacionalidade',)
    search_fields = ('nome',)
    list_filter = ('nacionalidade',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = (
    'titulo',
    'isbn',
    'pagina',
    'preco',
    'ano_publicacao',
    'capa',
    'estoque',
    'disponivel',
    'sinopse',
    'criado_em' ,
    'atualizado_em',
    )
    list_filter = ('categoria','editora','disponivel','ano_publicacao',)
    search_fields = ('titulo', 'isbn', 'autores_nome',)




