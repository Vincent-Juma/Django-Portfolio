from django.shortcuts import render
from imagegallery.models import imggal
from .models import Post

def imagedisplay(request):
    resultsdisplay=imggal.objects.all()
    return render(request,'imagegallery/gallery.html',{'imggal':resultsdisplay })

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'imagegallery/home.html', context)

def about(request):
    return render(request, 'imagegallery/about.html', {'title': 'About'})

def contacts(request):
    return render(request, 'imagegallery/contacts.html', {'title': 'Contacts'})

def info(request):
    return render(request, 'imagegallery/info.html', {'title': 'Info'})

def career(request):
    return render(request, 'imagegallery/career.html', {'title': 'Career'})


