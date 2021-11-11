FROM phusion/baseimage:latest
MAINTAINER Tudor Golubenco <tudor@packetbeat.com>


RUN apt-get update && apt-get -y -q install libpcap0.8 wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#ENV VERSION=5.5.2
ARG VERSION
ENV ARCH=x86_64 EXTENSION=tar.gz
ENV FILENAME=packetbeat-${VERSION}-linux-${ARCH}.${EXTENSION}

#https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.5.2-linux-x86_64.tar.gz
RUN wget https://artifacts.elastic.co/downloads/beats/packetbeat/${FILENAME}
RUN tar zxvf ${FILENAME}

# Required ? when we are using consul-template for that ?
#ADD packetbeat.yml /conf/packetbeat.yml
WORKDIR packetbeat-${VERSION}-linux-${ARCH}
VOLUME /conf

CMD ["./packetbeat", "-e", "-c=/conf/packetbeat.yml"]
