#As views servem para conectar os modelos e os templates

from django.shortcuts import redirect   # redireciona
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm   # para chamar o formulario


#O ponto antes de models significa diretório atual ou aplicativo atual. Tanto views.py como models.py estão no mesmo diretório.
#Isto significa que podemos usar . e o nome do arquivo (sem py).

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):  # view de detalhes da pág
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request): # view do formulario

    # condição para quando o página for acessada pela primeira vez e queremos um formulário em branco e,
    # quando voltamos para a view com todos os dados do formulário que acabamos de digitar.

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # redireciona para o post recem criado
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):  # view para editar um post
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})