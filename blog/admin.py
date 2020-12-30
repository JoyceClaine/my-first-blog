#a pág admin permite inserir, alterar e deletar os posts do blog

from django.contrib import admin
from .models import Post   #chama o Post criado no arquivo models.py

admin.site.register(Post)  #para tornar visivel o modelo Post na pág de administração