from django.shortcuts import render

# Create your views here.
from posts.forms import PostForm
from posts.models import Post


def posts(request):
    all_posts = Post.objects.all()
    context = {
        "posts": all_posts
    }
    return render(request, "posts.html", context)


def post_creation(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = PostForm()
        context = {
            "form": form
        }
        return render(request, "posts/post_creation.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, "posts/post_detail.html", context)
