# Cria um formulário para a pág do site

from django import forms  # importa o módulo de formulários do Django
from .models import Post  # importa  modelo Post


class PostForm(forms.ModelForm):  # modelo do formulario

    class Meta:  # classe que diz qual modelo usar para criar o formulario
        model = Post  # usaremos o nosso modelo post para criar o formulario
        fields = ('title', 'text',)  # esses serão os campos criados no formulario