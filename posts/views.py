from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import redirect
from posts.forms import PostForm



def word(request):
    if request.method == 'GET':
        return HttpResponse('Hello my friend. You play dota 2?')

def main_page(request):
    if request.method == 'GET':
        return render(request, template_name='main_page.html')

@login_required(login_url='login')
def post_list_view(request):
    posts = Post.objects.all()
    if request.method == 'GET':
       return render(request, template_name='posts/post_list.html', context={'posts': posts})

@login_required(login_url='login')
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method =='POST':
        # Post.objects.create(
        # image=image,
        # title=title,
        # content=content,
        # rate=rate
        # )
        return redirect('/posts/')