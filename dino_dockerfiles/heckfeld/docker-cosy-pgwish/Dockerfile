FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

# install everything for building and running
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install autoconf automake libtool \
		build-essential g++ \
		libpq-dev libx11-dev libxmu6 libxmu-dev \
		libxmu-headers libxpm-dev \
		xfonts-100dpi xfonts-75dpi \
		libpcap-dev libpq-dev \
		wmctrl libpgtcl libncurses5-dev git sudo

# build and install
RUN cd /tmp && \
    git clone https://github.com/heckfeld/cosy-pgwish.git && \
    cd cosy-pgwish && \
    autoreconf -iv && \
    ./configure --prefix=/usr --sysconfdir=/etc && \
    make install

# setup cosy environment
RUN cd /tmp && \
    git clone https://github.com/heckfeld/cosy-addr-server.git && \
    cd cosy-addr-server && \
    autoreconf -iv && \
    ./configure --prefix=/usr --sysconfdir=/etc  && \
    make install
    
RUN cd /tmp && \
    git clone https://github.com/heckfeld/cosy-sw-timing.git && \
    cd cosy-sw-timing && \
    autoreconf -iv && \
    ./configure --prefix=/usr --sysconfdir=/etc  && \
    make install
    
# setup addr_serv
RUN cd /tmp && \
    git clone https://github.com/heckfeld/cosy-setup.git && \
    cd cosy-setup && \
    autoreconf -iv && \
    ./configure --prefix=/usr --sysconfdir=/etc  && \
    chmod +x genconf && make install

# Cleanup everything used for building
RUN apt-get -y remove --purge autoconf automake libtool build-essential gcc g++ git ; \
    apt-get -y autoremove --purge
RUN cd /tmp && \
    rm -fr cosy-pgwish \
           cosy-addr-server \
           cosy-sw-timing \
           cosy-setup
COPY guis.conf /mnt/cc-x/cc-x3/coob/conf/
COPY hosts /mnt/cc-x/cc-x3/coob/conf/

# CMD /bin/bash
