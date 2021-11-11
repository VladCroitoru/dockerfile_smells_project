FROM ubuntu:latest

ENV VERSION=1.0.0-beta2 ARCH=x86_64 EXTENSION=tar.gz 
ENV PKBT_NAME=packetbeat-${VERSION}-${ARCH}.${EXTENSION} 

RUN \
  apt-get update && \
  apt-get install -y libpcap0.8 wget

RUN \
  cd / && \
  wget https://download.elastic.co/beats/packetbeat/$PKBT_NAME && \
  tar xvzf $PKBT_NAME && \
  rm -f $PKBT_NAME && \
  mv /packetbeat-${VERSION} /packetbeat

VOLUME ["/conf"]
WORKDIR packetbeat
COPY ./conf/packetbeat.yml /conf/packetbeat.yml

CMD ["./packetbeat", "-e", "-c=/conf/packetbeat.yml"]