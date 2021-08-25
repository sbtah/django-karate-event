from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def home(request):

    context = {

    }

    return render(request, 'application/home.html', context)


def post_list(request):

    posts_list = Post.objects.all()

    p = Paginator(Post.objects.all(), 1)
    page = request.GET.get('page')
    posts = p.get_page(page)

    context = {
        'posts_list': posts_list,
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
            return HttpResponseRedirect('/posts/?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, 'application/create_post.html', context)


def update_post(request, pk):

    post = Post.objects.get(pk=pk)

    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()

        return redirect('/posts')

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'application/update_post.html', context)


def delete_post(request, pk):

    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('/posts')
