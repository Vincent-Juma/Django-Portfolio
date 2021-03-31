from django.shortcuts import render
from imagegallery.models import imggal

def imagedisplay(request):
    resultsdisplay=imggal.objects.all()
    return render(request,'gallery.html',{'imggal':resultsdisplay })
