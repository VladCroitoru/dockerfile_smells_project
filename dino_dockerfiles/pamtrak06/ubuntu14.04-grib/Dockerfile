FROM ubuntu:14.04
MAINTAINER pamtrak06@gmail.com
RUN apt-get update -y && apt-get install -y wget curl locate git
RUN apt-get install -y rpm build-essential cmake gfortran
RUN apt-get install -y openjpeg-tools libgomp1 m4
ENV GRIBAPI_VERSION=1.15.0
#ENV GRIBAPI_VERSION=1.14.7
RUN wget https://software.ecmwf.int/wiki/download/attachments/3473437/grib_api-${GRIBAPI_VERSION}-Source.tar.gz?api=v2 -O grib_api-${GRIBAPI_VERSION}-Source.tar.gz
RUN tar -xvf grib_api-${GRIBAPI_VERSION}-Source.tar.gz
RUN mkdir -p /build/gribapi && mkdir -p /grib/gribapi

#WORKDIR /build/gribapi
#RUN cmake  /grib_api-${GRIBAPI_VERSION}-Source  -DCMAKE_INSTALL_PREFIX=/grib/gribapi
##RUN make && ctest && make install
#RUN make && make install

WORKDIR /grib_api-${GRIBAPI_VERSION}-Source
#RUN ./configure --prefix=/grib/gribapi --with-openjpeg="/usr/lib/x86_64-linux-gnu/libjpeg.so.8"
RUN ./configure --prefix=/grib/gribapi --disable-jpeg
#RUN make && make check && make install
RUN make && make install

# install libs4 cdo
RUN mkdir -p /build/cdo/libs4 && mkdir -p /grib/cdo/libs4
WORKDIR /build/cdo/libs4
RUN wget https://code.zmaw.de/attachments/download/10301/libs4cdo-0.0.11.tar.gz
RUN tar -xvf libs4cdo-0.0.11.tar.gz
RUN cd libs4cdo*/ && make libs4cdo

# install netcdf
RUN mkdir /build/netcdf && mkdir /grib/netcdf
WORKDIR /build/netcdf
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.0.tar.gz
RUN tar -xvf netcdf-4.4.0.tar.gz
RUN cd netcdf*/ && ./configure --enable-cxx-4 &&  autoreconf -if 
#RUN doxygen

# install CDO
WORKDIR /build/cdo
RUN wget https://code.zmaw.de/attachments/download/12692/cdo-current.tar.gz
RUN tar -xvf cdo-current.tar.gz
RUN cd cdo*/ && ./configure --prefix=/grib/cdo --with-netcdf=/grib/netcdf --with-grib_api=/grib/gribapi && make && make install

RUN updatedb
RUN chmod  755 /grib/gribapi/bin/*
RUN chmod  755 /grib/cdo/bin/*
ENV PATH=$PATH:/grib/gribapi/bin:/grib/cdo/bin
VOLUME /grib
WORKDIR /grib
