from django.urls import path

from webapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('base/', base, name='base'),
]