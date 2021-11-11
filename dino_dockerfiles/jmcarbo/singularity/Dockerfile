FROM ubuntu
RUN apt-get update
RUN apt-get -y install build-essential curl git sudo man vim autoconf libtool
RUN apt-get -y install python
RUN git clone https://github.com/singularityware/singularity.git
RUN cd singularity && ./autogen.sh && ./configure --prefix=/usr/local && make && make install
