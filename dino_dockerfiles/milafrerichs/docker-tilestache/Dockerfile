FROM ubuntu:14.04
MAINTAINER Mila Frerichs

# install Python and all the mapnik dependencies
RUN apt-get update -y && apt-get install -y libjpeg-dev zlib1g-dev python python-setuptools python-dev python-pip python-gdal libboost-python-dev software-properties-common libmapnik2.2 libmapnik-dev mapnik-utils python-mapnik python-psycopg2

# symlink the native extensions so Python can pick them up
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_python.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libboost_thread.so /usr/lib

# install tilestache, mapnik, and dependencies
RUN pip install --allow-external PIL --allow-unverified PIL PIL tilestache simplejson werkzeug sympy Blit mapnik2 shapely
