#As views servem para conectar os modelos e os templates

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#O ponto antes de models significa diretório atual ou aplicativo atual. Tanto views.py como models.py estão no mesmo diretório.
#Isto significa que podemos usar . e o nome do arquivo (sem py).

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):  # view de detalhes da pág
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
