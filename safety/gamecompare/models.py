from django.db import models
from django.contrib.gis.db import models as gismodels

class Cities(gismodels.Model):
	"""
	store the geodata for a city
	"""
	cityid = models.IntegerField()
	name = models.CharField(max_length=255)
	geom = gismodels.PolygonField()
	objects = gismodels.GeoManager()