FROM ubuntu:trusty

MAINTAINER cybermans <cybermans@gmail.com>

ENV SICKBEARD_VERSION master

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >> /etc/apt/sources.list 
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:mosquitto-dev/mosquitto-ppa && \
    apt-get update && \
    apt-get -y install python-cheetah curl mosquitto-clients && \
    apt-get -y autoremove && \
    apt-get -y clean

RUN curl -L https://github.com/midgetspy/Sick-Beard/tarball/$SICKBEARD_VERSION -o sickbeard.tgz && \
    tar -xvf sickbeard.tgz -C /  &&\
    mv /midgetspy-Sick-Beard-* /sickbeard/ &&\
    rm  /sickbeard.tgz

RUN mkdir -p /config && \
    mkdir -p /data

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

EXPOSE 8081

VOLUME ["/config"]
VOLUME ["/data"]


CMD ["/start.sh"]