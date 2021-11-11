# Python libSUMO Docker Image

FROM ubuntu:18.04
MAINTAINER Benjamin Striner <bstriner@andrew.cmu.edu>

## Basics
RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common
RUN apt-get install -y apt-utils
RUN apt-get install -y gcc
RUN apt-get install -y make
RUN apt-get install -y cmake
RUN apt-get install -y build-essential
RUN apt-get install -y git
RUN dpkg --configure -a

## Python
RUN apt-get install -y python3 python3-dev python3-pip
RUN python3 -m pip install --upgrade pip

## SUMO Dependencies
# Swig
RUN apt-get install -y swig
# XercesC
RUN apt-get install -y libxerces-c-dev
# GDAL
RUN apt-get install -y libgdal-dev
# proj
RUN apt-get install -y libproj-dev
# FOX
RUN apt-get install -y libfox-1.6-0 libfox-1.6-dev

## SUMO Install
WORKDIR /home
# RUN git clone https://github.com/eclipse/sumo.git
RUN git clone -b libsumo_close https://github.com/bstriner/sumo-1.git sumo
RUN cd sumo && mkdir build36 && cd build36 && cmake -DPython_ADDITIONAL_VERSIONS=3.6 -DCMAKE_BUILD_TYPE=Release .. && cmake --build . --target install_pylibsumo --config Release
