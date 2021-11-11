#
# Provide advanced networking tools for a RHEL/CentOS environment
#
FROM centos

MAINTAINER Scott McCarty <scott.mccarty@gmail.com>

RUN yum install -y wget git gcc make;yum clean all; wget http://tweegy.nl/download/netstat-nat-1.4.10.tar.gz; tar xvfz netstat-nat-1.4.10.tar.gz; cd netstat-nat-1.4.10; ./configure; make; make install; cd ..; git clone https://github.com/jbenc/plotnetcfg.git; wget  http://www.digip.org/jansson/releases/jansson-2.7.tar.gz; tar xvfz jansson-2.7.tar.gz; cd jansson-2.7; ./configure; make; cd ../plotnetcfg; make jansson=../jansson-2.7; make install; cd ..; rm -rf janson* plotnetcfg* netstat-nat*; yum -y autoremove wget git gcc make; yum clean all
