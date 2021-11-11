FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install -y \
      build-essential \
      wget \
      unzip \
      automake \
      libgdal-dev \
      libfcgi-dev \
      libssl-dev \
      unixodbc-dev \
      libmysqlclient-dev \
      libopencv-dev \
      lighttpd

RUN mkdir -p /build/poco
RUN wget -O /build/poco/poco.tar.gz http://pocoproject.org/releases/poco-1.6.0/poco-1.6.0-all.tar.gz
RUN cd /build/poco && \
    tar xvf poco.tar.gz && \
    cd poco-* && \
    ./configure && \
    make && \
    make install

RUN mkdir -p /build/gdal-correlator
RUN wget https://github.com/dudaerich/GDAL-correlator/archive/issue1.zip -O /build/gdal-correlator/gdal-correlator.zip
RUN cd /build/gdal-correlator && \
    unzip gdal-correlator.zip && \
    cd * && \
    autoreconf -i && \
    ./configure && \
    make && \
    make install

RUN ldconfig /usr/local/lib

COPY lighttpd-autogeoreference.conf /etc/lighttpd/conf-available/30-autogeoreference.conf
RUN lighttpd-enable-mod fastcgi
RUN lighttpd-enable-mod autogeoreference

COPY fcgi /build/fcgi
RUN cd /build/fcgi && make -e CONF=Release

COPY web /var/www/html

EXPOSE 80

COPY init.sh /init.sh
ENTRYPOINT ["/init.sh"]
