from django.shortcuts import render

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
	pass