
FROM ubuntu:16.04

MAINTAINER Quentin Peten

ENV USER mosquitto
ENV UID 1000

RUN apt-get update -q && \
       apt-get install -qy \
       mosquitto mosquitto-clients

RUN usermod -u $UID $USER && \
       apt-get autoremove -qy wget && \
       rm -rf /var/lib/apt/lists/*

USER $USER

VOLUME /config

CMD /usr/sbin/mosquitto -c /config/mosquitto.conf
