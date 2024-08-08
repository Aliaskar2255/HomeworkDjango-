from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def word(request):
    return HttpResponse('Hello my friend. You play dota 2?')

def main_page(request):
    return render(request, template_name='main_page.html')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, template_name='post_list.html', context={'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', context={'post': post})