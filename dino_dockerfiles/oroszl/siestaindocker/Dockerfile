FROM ubuntu:14.04.5

RUN apt-get update && apt-get upgrade -y
RUN apt-get install wget vim gfortran\
                    openmpi-common openmpi-bin \
                    libopenmpi-dev libblacs-mpi-dev \
                    libhdf5-dev \
                    libblas-dev liblapack-dev make ssh m4 mc python3-pip  locate -y
RUN updatedb

WORKDIR /opt
# Get netcdf scalapack and siesta
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz
RUN tar -xzvf netcdf-4.4.1.1.tar.gz
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-fortran-4.4.4.tar.gz
RUN tar -xzvf netcdf-fortran-4.4.4.tar.gz
RUN wget http://www.netlib.org/scalapack/scalapack-2.0.2.tgz
RUN tar -xzvf scalapack-2.0.2.tgz 
RUN wget https://launchpad.net/siesta/4.1/4.1-b2/+download/siesta-4.1-b2.tar.gz
RUN tar -xzvf siesta-4.1-b2.tar.gz

# build and install scalapack and netcdf
WORKDIR /opt/netcdf-4.4.1.1
RUN ./configure && make && make install
WORKDIR /opt/netcdf-fortran-4.4.4
RUN ./configure && make && make install
WORKDIR /opt/scalapack-2.0.2
RUN cp SLmake.inc.example SLmake.inc
RUN make lib
RUN cp libscalapack.a /usr/lib/
# build and install siesta
WORKDIR /opt/siesta-4.1-b2/Obj
RUN sh ../Src/obj_setup.sh
ADD arch.make ./
RUN make

ENV LD_LIBRARY_PATH /usr/local/lib


WORKDIR /opt
RUN pip3 install setuptools -U
RUN pip3 install ipython numpy -U
RUN pip3 install sisl





