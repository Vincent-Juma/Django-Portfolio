from django.shortcuts import render, redirect
from imagegallery.models import imggal, Image, Category, Location
from .models import Post
from django.http import Http404

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

def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    print(images)
    return render(request,'index.html',{'images':images,'locations':locations})

def display_location(request,location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id = location_id)
        images = Image.objects.filter(image_location = location.id)
    except:
        raise Http404()
    return render(request,'location.html',{'location':location,'images':images,'locations':locations})

def search_category(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Image.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'images':searched_images,'locations':locations})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message,'locations':locations})
