FROM phusion/baseimage:0.9.19
MAINTAINER manu <manu.bocquet@gmail.com>

ENV APTLIST="build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev uuid-dev wget" 
ENV SYSLOG_ADDR="192.168.1.5:514"
RUN adduser --system --disabled-password mosquitto

# install main packages
RUN apt-get update -q && \
apt-get install $APTLIST -qy

# Compile and install
RUN mkdir -p /usr/local/src
WORKDIR /usr/local/src
RUN wget http://mosquitto.org/files/source/mosquitto-1.4.10.tar.gz
RUN tar xvzf ./mosquitto-1.4.10.tar.gz
WORKDIR /usr/local/src/mosquitto-1.4.10
RUN make && make install

# cleanup
RUN dpkg -P build-essential wget && \
        apt-get -y autoremove && \
		apt-get clean -y && \
		rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Prepare docker
RUN mkdir /config
RUN mkdir -p /etc/service/mosquitto
ADD ./init.sh /etc/service/mosquitto/run
RUN chmod 755 /etc/service/mosquitto/run

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ports and volumes
EXPOSE 1883
VOLUME [ "/config" ]
