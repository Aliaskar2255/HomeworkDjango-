from django.shortcuts import render
from django.http import HttpResponse


def word(request):
    return HttpResponse('Hello my friend. You play dota 2?')

def main_page(request):
    return render(request, template_name='main_page.html')