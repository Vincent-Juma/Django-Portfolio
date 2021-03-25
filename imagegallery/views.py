from django.shortcuts import render
from imagegallery.models import imggal

def imagedisplay(request):
    resultsdisplay=imggal.objects.all()
    return render(request,'index.html',{'imggal':resultsdisplay })

def index(request):
    return render(request, 'imagegallery/index.html', {'title': 'Gallery'})