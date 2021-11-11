FROM inthecloud247/kdocker-base:latest
MAINTAINER John Albietz "inthecloud247@gmail.com"

RUN apt-get -y install python-dev python-twisted

RUN apt-get -y install libboost-dev libboost-test-dev libboost-program-options-dev libevent-dev automake libtool flex bison pkg-config g++ libssl-dev

RUN apt-get -y install python-pip; \
  pip install gevent bottle simplejson hive_utils

RUN wget http://mirror.olnevhost.net/pub/apache/thrift/0.9.1/thrift-0.9.1.tar.gz

# RUN mv *.*gz /files

# tar -xvf thrift-*
