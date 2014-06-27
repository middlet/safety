from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from gamecompare.models import Cities
from django.contrib.gis.geos import Polygon, GEOSGeometry

import json

class Command(BaseCommand):
    args = 'datafile.json'
    help = 'ingest geojson city polygons into the database'

    def handle(self, *args, **options):
        if len(args)==0:
            return
        with open(args[0]) as f:
                text = f.read()
        j = json.loads(text)
        #
        for fi in j['features']:
            name = fi['properties']['name']
            coords = fi['geometry']['coordinates']
            poly = Polygon(coords[0])
            obj, created = Cities.objects.get_or_create(name=name, geom=GEOSGeometry(poly.wkt))

