FROM ubuntu:16.04

USER root
WORKDIR /root

RUN apt-get update -y \
    && apt-get upgrade -y   \
    && apt-get dist-upgrade -y \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        build-essential \
        curl \
        iproute2 \
        iputils-ping \
        openvswitch-testcontroller \
        net-tools \
        tcpdump \
        vim \
        x11-xserver-utils \
        xterm   \
        git     \
        sudo 

RUN git clone git://github.com/mininet/mininet \
    && cd mininet \
    && git checkout -b 2.2.2 \
    && cd .. \
    && mininet/util/install.sh

ENV TERM xterm-color

#Getting the Repo for Entrypoint script
WORKDIR /
RUN git clone https://github.com/prashplus/mininet-docker
RUN ["chmod", "+x", "/mininet-docker/script/entrypoint.sh"]

# ENTRYPOINT script
ENTRYPOINT ["mininet-docker/script/entrypoint.sh"]