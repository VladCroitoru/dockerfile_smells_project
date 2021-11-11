# DockertFile for the Massive-PotreeConverter
FROM ubuntu:16.04
MAINTAINER Gijs van den Oord <g.vandenoord@esciencecenter.nl>
RUN apt-get update -y

# INSTALL compilers and build toold
RUN apt-get install -y apt-utils software-properties-common git cmake build-essential gcc g++ python-numpy python-dev python-pip lsb

# INSTALL libraries
RUN apt-get install -y libboost-all-dev libncurses5-dev libncursesw5-dev freeglut3-dev qtdeclarative5-dev libqwt-dev libqwt-headers xsdcxx
RUN pip install --upgrade pip
RUN pip install docopt
RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt-get update
RUN apt install -y libgdal-dev gdal-bin python-gdal libgdal20 
# Configure & build
WORKDIR /opt
RUN git clone https://github.com/pcraster/pcraster.git
WORKDIR /opt/pcraster
RUN git submodule update --init --recursive
RUN mkdir build
WORKDIR /opt/pcraster/build
RUN cmake .. -DGDAL_LIBRARY=/usr/lib/libgdal.so.20 -DGDAL_INCLUDE_DIR=/usr/include/gdal -DCMAKE_CXX_FLAGS="-Wno-deprecated"
RUN make
RUN make install
