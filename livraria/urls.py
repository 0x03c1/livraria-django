from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('sau/', views.saudacao, name='saudacao'),
    path('sau/teste', views.saudacaotest, name='saudacaotest'),
]