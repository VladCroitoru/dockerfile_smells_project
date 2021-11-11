FROM perl:latest

MAINTAINER Ross Dargan dockermaintainer@the-dargans.co.uk

WORKDIR /var/

RUN git clone https://github.com/nickandrew/LS30.git

WORKDIR /var/LS30

ENV PERLLIB $PERLLIB:/var/LS30/lib

VOLUME /var/LS30/devices/

ENV LS30_DEVICES=/var/LS30/devices/devices.yaml

RUN cpanm Date::Format YAML AnyEvent

#RUN groupadd -r alarmuser && useradd -r -g alarmuser alarmuser

#USER  alarmuser



CMD ["/var/LS30/bin/list-devices.pl", "-y"]

