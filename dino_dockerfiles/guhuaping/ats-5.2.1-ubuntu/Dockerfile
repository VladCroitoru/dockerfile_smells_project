FROM guhuaping/ats-ubuntu-base

MAINTAINER Huaping Gu <humphrey.gu@gmail.com>


#download ATS 5.2.0 and unzip
RUN wget http://mirror.metrocast.net/apache/trafficserver/trafficserver-5.2.1.tar.bz2
RUN tar -xvf trafficserver-5.2.1.tar.bz2

#config
RUN autoreconf -if /trafficserver-5.2.1/configure.ac
RUN /trafficserver-5.2.1/configure --enable-experimental-plugins --prefix=/opt/ats
#make
RUN make
RUN make check
#install
RUN sudo make install

#use default ATS port
EXPOSE 8080 
