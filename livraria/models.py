from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique =True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering =  ['nome']

    def __str__(self):
        return self.nome

class Editora (models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100, blank=True)
    site = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering =  ['nome']

    def __str__(self):
        return self.nome

class Autor (models.Model):
    nome = models.CharField(max_length=150)
    biografia = models.TextField(blank=True)
    nacionalidade =  models.CharField (max_length=60, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering =  ['nome']
    
class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    isbn =  models.CharField ('ISBN', max_length=20, unique=True)
    pagina = models.PositiveIntegerField('Páginas', default = 0)
    preco = models.DecimalField('Preço', max_digits= 8, decimal_places=2)
    ano_publicacao = models.PositiveIntegerField('Ano de publicação')
    capa = models.ImageField('Capa', upload_to= 'capas/', blank=True, null=True)
    estoque = models.PositiveBigIntegerField('Estoque', default=0)
    disponivel = models.BooleanField('Disponivel', default =True)
    sinopse = models.TextField('Sinopse', blank = False)
    criado_em = models.DateTimeField(auto_now_add= True)
    atualizado_em = models.DateTimeField(auto_now_add= True)

    categoria = models.ForeignKey (
        Categoria,
        on_delete = models.PROTECT,
        related_name = 'livros',
        verbose_name = "Categoria"
    )
    editora = models.ForeignKey(
        Editora,
        on_delete = models.PROTECT,
        related_name = 'livros',
        verbose_name = 'Editora'
    )

    autor = models.ManyToManyField(
        Autor,
        related_name = 'livros',
        verbose_name = 'Autor'
    )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering =  ['titulo']

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reversed ('livros: detalhe', kwargs= {'pk': self.pk})


# Create your models here.
