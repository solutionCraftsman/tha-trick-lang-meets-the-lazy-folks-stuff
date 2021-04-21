from django.shortcuts import render

from .models import Post
from .form import PostForm


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'post': posts
    }

    return render(request, 'post/home.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

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
