# ubuntu build + java 8 + maven + sbt + zmq + jzmq
FROM java:8

USER root

RUN useradd -m build

RUN apt-get update && apt-get install -y pkg-config libtool libtool-bin autoconf automake g++ make


USER build

WORKDIR /home/build

RUN git clone git://github.com/jedisct1/libsodium.git

WORKDIR /home/build/libsodium

RUN ./autogen.sh

RUN ./configure && make

USER root

WORKDIR /home/build/libsodium

RUN make install; ldconfig


USER build

WORKDIR /home/build

RUN git clone git://github.com/zeromq/libzmq.git

WORKDIR /home/build/libzmq

RUN ./autogen.sh

RUN ./configure && make

USER root

WORKDIR /home/build/libzmq

RUN make install; ldconfig


USER build

WORKDIR /home/build

RUN git clone git://github.com/zeromq/czmq.git

WORKDIR /home/build/czmq

RUN ./autogen.sh

RUN ./configure && make

USER root

WORKDIR /home/build/czmq

RUN make install; ldconfig


USER build

WORKDIR /home/build

RUN git clone git://github.com/zeromq/libcurve.git

WORKDIR /home/build/libcurve

RUN sh autogen.sh; ./autogen.sh; ./configure && make

USER root

WORKDIR /home/build/libcurve

RUN make install; ldconfig


RUN echo deb 'http://dl.bintray.com/sbt/debian /' | tee -a /etc/apt/sources.list.d/sbt.list

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823

RUN apt-get update; apt-get upgrade -y

RUN apt-get install -y sbt


USER build

WORKDIR /home/build

RUN wget http://apache-mirror.rbc.ru/pub/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz

RUN tar -xzf apache-maven-3.3.9-bin.tar.gz; mkdir /home/build/bin; ln -s /home/build/apache-maven-3.3.9/bin/mvn /home/build/bin/mvn;

RUN rm /home/build/apache-maven-3.3.9-bin.tar.gz


RUN git clone git://github.com/zeromq/jzmq.git

WORKDIR /home/build/jzmq/jzmq-jni

RUN ./autogen.sh; ./configure; make

USER root

WORKDIR /home/build/jzmq/jzmq-jni

RUN make install

USER build

WORKDIR /home/build/jzmq

RUN /home/build/bin/mvn install -DskipTests=true -Dgpg.skip=true

USER root

WORKDIR /home/build

RUN rm -R czmq  jzmq  libcurve  libsodium  libzmq

USER build

RUN sbt sbtVersion
