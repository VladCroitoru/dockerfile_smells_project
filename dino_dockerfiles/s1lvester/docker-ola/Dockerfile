FROM ubuntu:16.04

ADD start.sh /start.sh
ADD supervisord.conf /etc/supervisord.conf

RUN apt-get -qq update &&\
    apt-get -qq install \
    libcppunit-dev libcppunit-dev uuid-dev pkg-config libncurses5-dev libtool\
    autoconf automake g++ libmicrohttpd-dev libmicrohttpd10 protobuf-compiler \
    libprotobuf-lite9v5 python-protobuf libprotobuf-dev libprotoc-dev zlib1g-dev \
    bison flex make libftdi-dev libftdi1 libusb-1.0-0-dev liblo-dev \
    libavahi-client-dev git avahi-daemon supervisor &&\
    git clone https://github.com/OpenLightingProject/ola.git /tmp/ola &&\
    cd /tmp/ola &&\
    autoreconf -i &&\
    ./configure \
        --enable-python-libs \
        --disable-all-plugins \
        --enable-artnet \
        --disable-root-check &&\
    make -j 2 &&\
    make install &&\
    ldconfig &&\
    cd / &&\
    mkdir -p /var/log/supervisord &&\
    mkdir -p /scripts &&\
    apt-get autoremove && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\
    chmod a+x /start.sh

EXPOSE 9090

ENTRYPOINT ["/start.sh"]
