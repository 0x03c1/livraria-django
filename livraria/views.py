from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1 style=color:red>hello world</h1>')

def saudacao(request):
    return HttpResponse('<a href="templates/index.html">Seja bem vindo ao nosso projeto Django!</a>')

def saudacaotest(request):
    return HttpResponse('<h1>Testando</h1>')
# Create your views here.
