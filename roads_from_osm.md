# ingesting road data

## getting the data

download the raw openstreet map data (http://download.geofabrik.de/). you can navigate to an individual country or region to get a subset. as an example Great Britain can be found (http://download.geofabrik.de/europe/great-britain.html|here). for convenience i used the shp file. there are a number of interal files including roads.* which contain the roads.

## converting the data to postgres
to convert from the shapefile to sql we can issue the following command:
```
shp2pgsql -s4326 ./roads.shp > roads.sql
```
this takes a while.

## creating the database
from within postgres we can issue the command:
```
\i roads.sql
```
even slower (:

## creating a dataset which has the midpoint of each road
getting the midpoint of each line is simple:

```
select st_centroid(geom) from roads where type='residential' and bridge=0 and tunnel=0;
```

this returns the midpoint of each road in the original data. we can export all the data to another table:

```
create table roads_centre as select gid,osm_id,name,ref,type,st_centroid(geom) as geom from roads where type='residential' and bridge=0 and tunnel=0;
```

export the data as a sql dump:
```
pg_dump -d safety -t roads_centre --inserts > roads_centre.sql
```
this will dump the specific table using insert commands to a sql file. this needs to be done on the command line.
