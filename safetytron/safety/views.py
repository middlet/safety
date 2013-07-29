import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


def home_page(request):
    # select a random set of coordinates for the images
    ll1 = _random_lat_long()
    ll2 = _random_lat_long()
    # render the resulting page
    return render(request, 'home.html', {
        'p1':ll1, 'p2':ll2,
    })
    

def update_on_click(request):
    if request.method == 'POST':
        return redirect('/')
    
    return home_page(request)


def _random_lat_long():
    # should return coords within a polygon
    lng = random.uniform(-0.489, 0.236)
    lat = random.uniform(51.28, 51.686)
    return [lat, lng]
