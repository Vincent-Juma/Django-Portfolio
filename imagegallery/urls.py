from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('info/', views.info, name='info'),
    path('career/', views.career, name='career'),
    url(r'^$',views.index,name='index'),
    url(r'^location/(\d+)',views.display_location,name='displayLocation'),
    url(r'^search/',views.search_category,name='search_category')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
