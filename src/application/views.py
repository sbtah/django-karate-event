from django.shortcuts import render
from .models import Post
from .forms import PostForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):

    month = month.capitalize()
    month_n = list(calendar.month_name).index(month)
    month_n = int(month_n)

    cal = HTMLCalendar().formatmonth(year, month_n)

    context = {
        'year': year,
        'month': month,
        'cal': cal,
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

    form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'application/create_post.html', context)
