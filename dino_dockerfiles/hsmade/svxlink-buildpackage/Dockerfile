FROM ubuntu:16.04
MAINTAINER Wim Fournier <wim@fournier.nl>

RUN apt-get update && apt-get install -y \
        git cmake g++ make libsigc++-2.0-dev libgsm1-dev \
        libpopt-dev tcl8.5-dev libgcrypt11-dev libspeex-dev \
        libasound2-dev alsa-utils vorbis-tools libqt4-dev \
        libopus-dev librtlsdr-dev groff doxygen checkinstall && \
    rm -rf /var/lib/apt/lists/*

COPY build.sh /
CMD ["/build.sh"]
VOLUME /package
