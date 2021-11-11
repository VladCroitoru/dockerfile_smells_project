FROM ubuntu:16.04

MAINTAINER Bitworks Software info@bitworks.software

ENV KVM_HOST qemu+tcp://root@10.252.1.35:16509/system
ENV INFLUX_HOST influxhost.com
ENV INFLUX_PORT 8086
ENV INFLUX_DB puls
ENV INFLUX_USER puls
ENV INFLUX_PASSWORD secret
ENV PAUSE 20
ENV GATHER_HOST_STATS true
ENV DEBUG true

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-libvirt python-influxdb openssh-client

COPY ./src /opt


WORKDIR /opt

CMD ["/bin/bash", "/opt/update-virt-hostinfo"]


