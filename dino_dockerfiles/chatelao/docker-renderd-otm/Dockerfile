# DOCKER-VERSION 1.3.1
# VERSION 0.1
FROM chatelao/docker-renderd-osm:opentopomap
# FROM ubuntu:16.04
MAINTAINER Olivier Chatelain <olivier.chatelain@gmail.com>

# RUN touch /etc/inittab
RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install -y -q \
#      curl  \
#      git \
      unzip \
      vim \
      wget \
      python-gdal \
      gdal-bin

RUN mkdir -p /usr/share/mapnik/osm-custom/hillshade
COPY srtm_list.txt /usr/share/mapnik/osm-custom/hillshade
RUN cd /usr/share/mapnik/osm-custom/hillshade && wget -i srtm_list.txt && for zipfile in *.zip;do unzip -j -o "$zipfile" -d unpacked; done
RUN cd /usr/share/mapnik/osm-custom/hillshade/unpacked && mv * ..

# Fill all voids
RUN cd /usr/share/mapnik/osm-custom/hillshade && for hgtfile in *.hgt;do gdal_fillnodata.py $hgtfile $hgtfile.tif; done

# Merge all .tifs into one huge tif. This file will is the raw DEM with full resolution and the start for any further steps.
# RUN cd /usr/share/mapnik/osm-custom/hillshade/unpacked && gdal_merge.py -n 32767 -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -o ../../raw.tif *.hgt.tif
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdal_merge.py -n 32767 -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -o raw.tif *.hgt.tif

# Convert the raw file into Mercator projection, interpolate and shrink
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdalwarp -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m" -r bilinear -tr 5000 5000 raw.tif warp-5000.tif
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdalwarp -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m" -r bilinear -tr 1000 1000 raw.tif warp-1000.tif
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdalwarp -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m" -r bilinear -tr  700  500 raw.tif  warp-700.tif
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdalwarp -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m" -r bilinear -tr  500  500 raw.tif  warp-500.tif
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdalwarp -co BIGTIFF=YES -co TILED=YES -co COMPRESS=LZW -co PREDICTOR=2 -t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m" -r bilinear -tr   90   90 raw.tif   warp-90.tif

#
#	Parameters:
#		-co BIGTIFF=YES: if output > 4 GB
#		-co TILED=YES: intern tiles
#		-co COMPRESS=LZW -co PREDICTOR=2: lossless compression with prediction
#		-t_srs "+proj=merc +ellps=sphere +R=6378137 +a=6378137 +units=m": convertion into Mercator
#		-r cubicspline: interpolation for tr < 90 m
#		   bilinear: for tr > 90 m
#		-tr 30 30: desired resolution in meter
#

#
# Get the current "relief.txt" from OpenTopoMap
#
RUN cd /usr/share/mapnik/osm-custom/hillshade/ && wget https://github.com/chatelao/OpenTopoMap/blob/master/mapnik/relief.txt
# COPY relief.txt /usr/share/mapnik/osm-custom/hillshade/unpacked

# Create color relief for different zoom levels
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdaldem color-relief -co COMPRESS=LZW -co PREDICTOR=2 -alpha warp-5000.tif relief.txt relief-5000.tif 
RUN cd /usr/share/mapnik/osm-custom/hillshade && gdaldem color-relief -co COMPRESS=LZW -co PREDICTOR=2 -alpha warp-500.tif  relief.txt relief-500.tif 

# Create hillshade for different zoom levels
# Note: gdaldem and gdalwarp have problems compressing huge files while generation. You can compress those afterwards by gdal_translate -co compress=...
RUN cd /usr/share/mapnik/osm-custom/hillshade \
  && gdaldem hillshade -z 7 -compute_edges -co COMPRESS=JPEG warp-5000.tif hillshade-5000.tif \
  && gdaldem hillshade -z 7 -compute_edges -co BIGTIFF=YES -co TILED=YES -co COMPRESS=JPEG warp-1000.tif hillshade-1000.tif \
  && gdaldem hillshade -z 4 -compute_edges -co BIGTIFF=YES -co TILED=YES -co COMPRESS=JPEG warp-700.tif hillshade-700.tif \
  && gdaldem hillshade -z 2 -co compress=lzw -co predictor=2 -co bigtiff=yes -compute_edges warp-90.tif hillshade-90.tif && gdal_translate -co compress=JPEG -co bigtiff=yes -co tiled=yes hillshade-90.tif hillshade-90-jpeg.tif


# Create contour lines
	# Install phyghtmap: sudo apt-get install python-setuptools python-matplotlib python-beautifulsoup python-numpy
	# wget http://katze.tfiu.de/projects/phyghtmap/phyghtmap_1.71.orig.tar.gz (or newer)
	# sudo python setup.py install
RUN apt-get install -y -q \
   python-setuptools \
   python-matplotlib \
   python-beautifulsoup \
   python-numpy	
RUN wget http://katze.tfiu.de/projects/phyghtmap/phyghtmap_1.74.orig.tar.gz \
   && tar -xvzf phyghtmap_1.74.orig.tar.gz \
   && cd phyghtmap-1.74 \
   && python setup.py install
RUN cd /usr/share/mapnik/osm-custom/hillshade && phyghtmap --max-nodes-per-tile=0 -s 10 -0 --pbf warp-90.tif

# # Create contours database
# 	sudo -u postgres -i
# 	createdb -E UTF8 -O username contours
# 	exit
# 	psql -f /usr/share/postgresql/9.3/contrib/postgis-2.1/postgis.sql -d contours
# 	psql -f /usr/share/postgresql/9.3/contrib/postgis-2.1/spatial_ref_sys.sql -d contours
# 	psql -d contours -c "ALTER TABLE geometry_columns OWNER TO username; ALTER TABLE spatial_ref_sys OWNER TO username;"
# 	#psql -f /usr/local/share/osm2pgsql/900913.sql -d contours

RUN cd /usr/share/mapnik/osm-custom/hillshade/ && wget https://github.com/chatelao/OpenTopoMap/blob/master/mapnik/osm2pgsql/contours.style

# # Load contour file into database
# 	screen osm2pgsql --slim -d contours -C 12000 --number-processes 10 --style ~/OpenTopoMap/mapnik/osm2pgsql/contours.style contours.pbf
