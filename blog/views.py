from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    posts = get_object_or_404(post,
                              status=Post.Status.PUBLISHED,
                              slug=post,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})