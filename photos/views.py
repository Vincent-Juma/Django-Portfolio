from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.

def welcome(request):

    photos=Image.objects.all()
    return render(request, 'all-photos/welcome.html', {"photos":photos})




def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})



def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

def search_by_location(request):
    if 'location'in request.GET and request.GET["location"]:
        search_term=request.GET.get("location")
        searched_images = Image.search_by_location(search_term)
        message = f"{search_term}"
        return render(request,'all-photos/location.html',{"message":message,"images": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/location.html',{"message":message})
        
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})
  