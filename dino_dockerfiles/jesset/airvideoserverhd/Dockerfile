FROM debian:latest
MAINTAINER Tian Congxin <tiancongxin@gmail.com>

ENV LANG C.UTF-8

#RUN echo 'deb http://mirrors.163.com/debian jessie main' > /etc/apt/sources.list
#RUN echo 'deb http://mirrors.163.com/debian jessie-updates main' >> /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends vlc-nox && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y wget bzip2 && \
    wget -qO - https://s3.amazonaws.com/AirVideoHD/Download/AirVideoServerHD-2.2.0.tar.bz2 | tar xjf - -C /opt && \
    apt-get purge -y wget bzip2 && apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

ADD Server.properties /opt/Server.properties
ADD run.sh /run.sh
EXPOSE 45633 45601

VOLUME ["/Movies", "/var/run/dbus/system_bus_socket"]

ENV DBUS_SYSTEM_BUS_ADDRESS  unix:path=/var/run/dbus/system_bus_socket
USER nobody

# CMD ["/opt/AirVideoServerHD", "--config=/opt/Server.properties"]
CMD ["/run.sh"]
