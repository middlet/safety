from django.shortcuts import render
from random import choice

import base64
import os
import requests
import StringIO

from .models import Cities, Roads, StreetViewImage

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
	point = [None, None]
	point[0] = choice(roads_points)
	point[1] = choice(roads_points)
	while point[1]==point[0]:
		point[1] = choice(roads_points)

	svurl = 'http://maps.googleapis.com/maps/api/streetview?size=400x400&location={},{}'
	images = [None, None]
	for pi, pt in enumerate(point):
		try:
			s = StreetViewImage.objects.get(url__exact=svurl.format(pt[1], pt[0]))
		except:
			s = StreetViewImage(url=svurl.format(pt[1], pt[0]))
			s.cache()
			image = s.streetimage.open()
			out = StringIO.StringIO()
			base64.encode(image, out)
			images[pi] = out.getvalue().replace('\n', '')

	context = {'im0':images[0], 'im1':images[1], 'pt0':point[0], 'pt1':point[1]}
	print 'final', point[0][0]-point[1][0], point[0][1]-point[1][1]
	# 
	return render(request, 'home.html', context)
