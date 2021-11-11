FROM debian:latest
MAINTAINER Evgeniy Slizevich <evgeniy@slizevich.net>

WORKDIR /

RUN apt-get update && \
    apt-get install -y git gcc make librtlsdr-dev pkg-config libusb-1.0-0-dev librtlsdr0 && \
    git clone https://github.com/mutability/dump1090.git /tmp/src && \
    cd /tmp/src && \
    make && \
    mkdir /usr/local/dump1090 && \
    mv dump1090 view1090 /usr/local/dump1090 && \
    cd / && rm -rf /tmp/src && \
    apt-get purge -y git gcc make pkg-config libusb-1.0-0-dev && \
    apt-get autoremove -y --purge && \
    rm -rf /var/lib/apt/lists/*

ADD dump1090 /dump1090

EXPOSE 30001 30002 30003 30004 30005 30104

VOLUME /dev/bus/usb

ENTRYPOINT ["/dump1090"]
