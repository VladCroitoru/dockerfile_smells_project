FROM phusion/baseimage:0.9.16

MAINTAINER Vojta Orgoň (villlem@gmail.com)

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Fix a Debianism of the nobody's uid being 65534
RUN usermod -u 99 nobody
RUN usermod -g 100 nobody

RUN add-apt-repository ppa:mosquitto-dev/mosquitto-ppa -y
RUN apt-get update
RUN apt-get install -y mosquitto mosquitto-clients

RUN mkdir -p /mosquitto/config
RUN mkdir -p /mosquitto/data
RUN mkdir -p /mosquitto/log

# RUN chown -R nobody:users /mosquitto

VOLUME ["/etc/mosquitto/config","/mosquitto/data","/mosquitto/log"]

ADD mosquitto-broker.sh /etc/service/mosquitto-broker/run

EXPOSE 1883
