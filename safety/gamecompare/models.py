from django.db import models
from django.contrib.gis.db import models as gismodels

class Cities(gismodels.Model):
	"""
	store the geodata for a city
	"""
	name = models.CharField(max_length=255)
	geom = gismodels.PolygonField()
	objects = gismodels.GeoManager()

class Roads(gismodels.Model):
	"""
	store a single point for the centre of each road 
	"""
	name = models.CharField(max_length=48, null=True)
	geom = gismodels.PointField()
	objects = gismodels.GeoManager()