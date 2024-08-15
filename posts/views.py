from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import redirect


def word(request):
    if request.method == 'GET':
        return HttpResponse('Hello my friend. You play dota 2?')

def main_page(request):
    if request.method == 'GET':
        return render(request, template_name='main_page.html')

def post_list_view(request):
    posts = Post.objects.all()
    if request.method == 'GET':
       return render(request, template_name='post_list.html', context={'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'post_detail.html', context={'post': post})

def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'post_create.html')
    if request.method =='POST':
        image=request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        rate = request.POST.get('rate')
        Post.objects.create(
        image=image,
        title=title,
        content=content,
        rate=rate
        )
        return redirect('/posts/')