FROM ubuntu:xenial

MAINTAINER cybermans <cybermans@gmail.com>
LABEL version 20180313

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
RUN echo "deb http://apt.sonarr.tv/ master main" | tee /etc/apt/sources.list.d/sonarr.list
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:mosquitto-dev/mosquitto-ppa && \
    apt-get update && \
    apt-get -y install nzbdrone mosquitto-clients tzdata && \
    apt-get -y autoremove && \
    apt-get -y clean


RUN mkdir -p /config && \
    mkdir -p /data

ADD mosquittonotifier.sh /bin/mosquittonotifier.sh
RUN chmod +x /bin/mosquittonotifier.sh

EXPOSE 8081

VOLUME ["/config"]
VOLUME ["/data"]

ENTRYPOINT ["/usr/bin/mono"]
CMD ["/opt/NzbDrone/NzbDrone.exe"]
