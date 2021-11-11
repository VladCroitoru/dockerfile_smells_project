FROM geographica/gdal2:2.1.2

MAINTAINER Nikki Aldeborgh <nikki.aldeborgh@digitalglobe.com>

RUN apt-get update -y && apt-get install -y \
    vim \
    ipython \
    python-pip

RUN pip install geojson

ADD ./bin /
