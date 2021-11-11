FROM debian:jessie-slim
MAINTAINER vistalba

# Set ENV
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /tmp

# Set Workdir
WORKDIR /tmp

# Install requirements
RUN apt-get update && apt-get install -y wget make gcc

# Install udpxy
RUN wget http://www.udpxy.com/download/udpxy/udpxy-src.tar.gz
RUN tar -xzvf udpxy-src.tar.gz
RUN cd udpxy* && make && make install

# Cleanup
RUN apt-get -qqy remove make gcc > /dev/null \
    && apt-get -qqy autoremove --purge > /dev/null \
    && apt-get -qqy clean autoclean > /dev/null \
    && rm -rf /var/cache/apt/* /var/cache/debconf/* /var/lib/apt/* /var/lib/dpkg/* /tmp/* /var/tmp/* /var/log/*

# Set start command
#CMD ["/usr/local/bin/udpxy", ${UDPXY_OPTS}]
ENTRYPOINT [ "sh", "-c", "/usr/local/bin/udpxy ${UDPXY_OPTS}" ]
