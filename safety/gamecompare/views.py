from django.shortcuts import render
from random import choice

import os
import requests

from .models import Cities, Roads

def debug(request, place):
	"""
	render a page displaying the data for a city
	"""
	# get the points inside the places polygon
	soton = Cities.objects.get(name__icontains=place)
	soton_points = [[pi[0],pi[1]] for pi in soton.geom.coords[0]]
	# find points in the polygon
	roads = Roads.objects.filter(geom__within=soton.geom)
	roads_points = [[ri.geom.coords[0],ri.geom.coords[1]] for ri in roads]
	# probably should pass this in via json
	context = {'roads':roads_points, 'poly':soton_points, 'bbox':soton.geom.extent, 'place':soton.name}
	#
	return render(request, 'debug.html', context)


def home(request):
	"""
	get the street view images and cache them for reuse later
	"""
	place = 'Southampton'
	# get polygon
	place = Cities.objects.get(name__icontains=place)
	# find the roads inside the polygon
	roads = Roads.objects.filter(geom__within=place.geom)
	roads_points = [[ri.geom.coords[0],ri.geom.coords[1]] for ri in roads]
	# get a random point
	point0 = choice(roads_points)
	point1 = choice(roads_points)
	while point1==point0:
		point1 = choice(roads_points)
	# base directory for image data
	base_dir = os.getcwd()
	base_dir = os.path.join(base_dir, 'images')
	# download the image from google street view
	gsv_url = 'http://maps.googleapis.com/maps/api/streetview?size=400x400&location=%f,%f'
	# get the images
	fname0 = os.path.join(base_dir, '%f,%f' % (point0[1], point0[0]))
	fname1 = os.path.join(base_dir, '%f,%f' % (point1[1], point1[0]))
	# load in parallel?
	if not os.path.isfile(fname0):
		im0 = requests.get(gsv_url%(point0[1],point0[0]))
		im0 = im0.content
		f = open(fname0, 'w')
		f.write(im0)
		f.close()
	else:
		f = open(fname0)
		im0 = f.read()
		f.close()
	if not os.path.isfile(fname1):
		im1 = requests.get(gsv_url%(point1[1],point1[0]))
		im1 = im1.content
		f = open(fname1, 'w')
		f.write(im1)
		f.close()
	else:
		f = open(fname1)
		im1 = f.read()
		f.close()
	context = {'im0':im0, 'im1':im1}
	# 
	return render(request, 'home.html', context)
