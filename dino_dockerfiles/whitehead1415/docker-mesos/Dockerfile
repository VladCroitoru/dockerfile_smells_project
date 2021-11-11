# Docker-Verson 0.7

From ubuntu
MAINTAINER Michael Whitehead <whitehead1415@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y -q autoconf make gcc cpp patch python-dev git libtool gzip libghc-zlib-dev libcurl4-openssl-dev build-essential default-jdk default-jdk-builddep default-jre libsasl2-dev
RUN apt-get -y install libunwind7-dev

ENV JAVA_HOME /usr/lib/jvm/java-1.6.0-openjdk-amd64/

RUN git clone https://github.com/apache/mesos.git
RUN (cd mesos && ./bootstrap)

RUN (cd mesos && ./configure --with-webui --with-included-zookeeper --disable-perftools)
RUN (cd mesos && make)
RUN (cd mesos && make install)
RUN (cp mesos/src/.libs/libmesos-0.16.0.so /usr/lib)

EXPOSE 5050

CMD ["mesos-master"]

