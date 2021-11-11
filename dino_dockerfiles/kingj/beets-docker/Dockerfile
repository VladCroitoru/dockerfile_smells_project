FROM ubuntu:18.04

ENV BEETSDIR /etc/beets/

RUN apt-get -y update && apt-get install -y \
  locales \
  python3-pip \
  bs1770gain \
  libchromaprint-tools \
  ffmpeg \
  curl

RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LANGUAGE en_GB:en  
ENV LC_ALL en_GB.UTF-8

RUN pip3 install \
  beets[fetchart,lastgenre,chroma,web]==1.4.9 \
  beets-extrafiles \
  flask
  
COPY config.yaml /etc/beets/config.yaml

EXPOSE 8337

VOLUME /etc/beets /music /import /convert

CMD beet web
