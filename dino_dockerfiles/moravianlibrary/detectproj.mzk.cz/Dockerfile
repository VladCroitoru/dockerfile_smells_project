FROM debian:wheezy

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y \
    lighttpd \
    build-essential \
    automake \
    libtool \
    wget \
    ca-certificates \
    unzip \
    libfcgi-dev \
    libjsoncpp-dev \
    libsqlite3-dev

RUN mkdir /build
RUN cd /build && \
    wget https://github.com/moravianlibrary/libalgo/archive/1.16.2.zip -O libalgo.zip && \
    unzip libalgo.zip && \
    cd libalgo-* && \
    libtoolize && \
    autoreconf -i && \
    ./configure && \
    make && \
    make install && \
    ldconfig /usr/local/lib

COPY lighttpd-detectproj.conf /etc/lighttpd/conf-available/30-detectproj.conf
RUN lighttpd-enable-mod fastcgi
RUN lighttpd-enable-mod detectproj

RUN mkdir detectproj
COPY projections.txt /usr/local/detectproj/projections.txt
COPY src/main.cpp /build/detectproj/main.cpp
COPY src/output.cpp /build/detectproj/output.cpp
COPY src/output.h /build/detectproj/output.h
COPY src/sqlite.cpp /build/detectproj/sqlite.cpp
COPY src/sqlite.h /build/detectproj/sqlite.h
COPY src/detectproj.cpp /build/detectproj/detectproj.cpp
COPY src/detectproj.h /build/detectproj/detectproj.h

RUN g++ /build/detectproj/*.cpp -ansi -O2 -lfcgi -ljsoncpp -lalgo -lsqlite3 -lm -o /usr/local/bin/detectproj

# sample-viewer
COPY sample-viewer/ajax-loader.gif /var/www/ajax-loader.gif
COPY sample-viewer/OpenLayers.js /var/www/OpenLayers.js
COPY sample-viewer/theme /var/www/theme
COPY sample-viewer/index.html /var/www/index.html
COPY sample-viewer/index.css /var/www/index.css
COPY sample-viewer/index.js /var/www/index.js

COPY init.sh /init.sh

ENTRYPOINT ["/init.sh"]
