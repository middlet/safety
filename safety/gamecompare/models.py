from django.db import models
from django.contrib.gis.db import models as gismodels
from django.core.files import File

import os
import urllib


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

class StreetViewImage(models.Model):
	"""
	grab an image via google street view and cache locally
	"""
	url = models.CharField(max_length=2000, unique=True)
	streetimage = models.ImageField(upload_to="gamecompare/images", blank=True)

	def cache(self):
		"""
		cache the image locally if we have a valid url
		"""
		print self.url
		if self.url and not self.streetimage:
			result = urllib.urlretrieve(self.url)
			fname = os.path.basename(self.url).split('&')[-1]+".jpg"
			print 'fname = ', fname, 'result = ', result
			self.streetimage.save(fname, File(open(result[0])))
			self.save()