from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Contacts'})

def info(request):
    return render(request, 'blog/info.html', {'title': 'Info'})

def career(request):
    return render(request, 'blog/career.html', {'title': 'Career'})

