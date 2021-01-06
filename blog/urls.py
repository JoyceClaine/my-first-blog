'''URLS é o caminho para onde as páginas devem ser direconadas'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #cria uma URL no arquivo blog/urls.py que aponta para uma view chamada post_detail, que vai nos mostrar o post completo.
]


# Entendendo a linha path('post/<int:pk>/', views.post_detail, name='post_detail')
# A parte post/<int:pk>/ especifica um padrão de URL – vamos explicar:

    # post/ significa apenas que a URL deve começar com a palavra post seguida por /. Até aqui, tudo bem.
    # <int:pk> – essa parte é um pouco mais complicada. Ela nos diz que o Django espera um objeto do tipo inteiro e que
    # vai transferi-lo para a view como uma variável chamada pk.
    #  / – por fim, precisamos adicionar uma / ao final da nossa URL.
