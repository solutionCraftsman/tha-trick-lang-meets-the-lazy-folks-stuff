from django.shortcuts import render

from .models import Post
from .form import PostForm


# Create your views here.
def all_posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'post/all.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = PostForm()
        return render(
            request,
            'post/create.html',
            {
                'form': form
            })


def details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post/details.html', context)
