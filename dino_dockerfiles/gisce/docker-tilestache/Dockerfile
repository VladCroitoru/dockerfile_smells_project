FROM ubuntu:14.04
MAINTAINER GISCE-TI, S.L. <devel@gisce.net>

RUN echo "deb http://ppa.launchpad.net/mapnik/nightly-2.3/ubuntu trusty main">>/etc/apt/sources.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 4F7B93595D50B6BA


# install Python and all the mapnik dependencies
RUN apt-get update -y && apt-get install -y libjpeg-dev zlib1g-dev python python-setuptools python-dev python-pip python-gdal libboost-python-dev software-properties-common libmapnik2.2 libmapnik-dev mapnik-utils python-mapnik nodejs-legacy npm mapnik-input-plugin-postgis libpq-dev

# symlink the native extensions so Python can pick them up
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_python.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_thread.so /usr/lib

RUN npm install -g https://github.com/gisce/carto/archive/extends_zoom_level.tar.gz

# install tilestache, mapnik, and dependencies
RUN pip install https://github.com/TileStache/TileStache/archive/master.zip sympy Blit uwsgi fabric osconf psycopg2 raven\<5.0
