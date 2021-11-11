FROM debian:jessie

# Allows to set-up HTTP(S) proxy using '--build-arg'
ARG http_proxy
ARG https_proxy

ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}

RUN echo $https_proxy
RUN echo $http_proxy

# Update and install core build tools
RUN apt-get update
RUN apt-get install -y \
    build-essential git scons libtool autoconf \
    valgrind doxygen wget unzip curl

# Install IoTivity build dependencies
RUN apt-get install -y \
    libboost-dev libboost-program-options-dev libboost-thread-dev \
    uuid-dev libexpat1-dev libglib2.0-dev libsqlite3-dev \
    libcurl4-gnutls-dev

# Install nodejs
# the node.js package in Debian Jessie official repositories is too
# old for iotivity-node (> 0.10 required and 0.10.29 provided)
RUN curl -sL https://deb.nodesource.com/setup_6.x | /bin/bash -
RUN apt-get install -y nodejs

# Create Home Gateway app directory
RUN mkdir -p /opt/IoTivity-in-a-box/
WORKDIR opt/IoTivity-in-a-box/

COPY . /opt/IoTivity-in-a-box/

RUN npm install

# Create mount point
VOLUME ["/opt/user/"]

# Unset proxy
ENV http_proxy ""
ENV https_proxy ""

# Start Home Gateway
ENTRYPOINT ["/opt/IoTivity-in-a-box/start-iotivity-node-in-docker.sh"]
