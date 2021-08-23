from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


def home(request):

    context = {

    }

    return render(request, 'application/home.html', context)


def post_list(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'application/post_list.html', context)


def post_detail(request, pk):

    post = Post.objects.get(pk=pk)

    context = {

        'post': post,
    }

    return render(request, 'application/post_detail.html', context)


def create_post(request):

    submitted = False

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'application/create_post.html', context)
