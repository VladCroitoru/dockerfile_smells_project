FROM ubuntu:16.04

RUN apt -y update && apt -y upgrade && apt install -y software-properties-common

RUN add-apt-repository -y ppa:ubuntugis/ppa
RUN apt -y update && apt -y upgrade

RUN apt install -y build-essential gcc-5-base libgcc-5-dev g++ clang libboost-all-dev

RUN apt install -y cmake wget git
            
RUN apt install -y libkml-dev libgdal-dev

RUN apt install -y libgmp-dev libmpfr-dev libmpfrc++-dev lib3ds-dev libtinyxml2-dev

WORKDIR /home
RUN wget https://github.com/CGAL/cgal/archive/releases/CGAL-4.10.tar.gz && mkdir -p CGAL-4.10 && tar xf CGAL-4.10.tar.gz -C CGAL-4.10 --strip-components 1 && mkdir -p CGAL-4.10/build
WORKDIR CGAL-4.10/build
RUN cmake .. -DCMAKE_INSTALL_PREFIX=/usr && make -j `nproc` install && make install_FindCGAL

RUN mkdir -p /home/proj.city
COPY . /home/proj.city
RUN mkdir -p /home/proj.city/build && mkdir -p /home/proj.city/build/xenial
WORKDIR /home/proj.city/build/xenial
