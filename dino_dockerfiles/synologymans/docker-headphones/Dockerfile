FROM ubuntu:xenial

MAINTAINER cybermans <cybermans@gmail.com>
LABEL version 20180313

RUN apt-get update && \
    apt-get -y install git python2.7 && \
    apt-get -y autoremove && \
    apt-get -y clean


RUN mkdir /config
COPY config.ini /config/config.ini
WORKDIR /opt
RUN git clone https://github.com/rembo10/headphones.git

WORKDIR /opt/headphones

VOLUME ["/config"]
EXPOSE 8181

CMD python2.7 /opt/headphones/Headphones.py --verbose --datadir /config
