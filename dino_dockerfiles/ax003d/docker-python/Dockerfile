FROM ubuntu:trusty

MAINTAINER ax003d <ax003d@gmail.com>

RUN apt-get update && \
    apt-get install -y python \
                       python-dev \
                       python-pip \
                       libmysqlclient-dev \
                       libxml2-dev \
                       libxslt1-dev \
                       libtiff4-dev \
                       libjpeg8-dev \
                       zlib1g-dev \
                       libfreetype6-dev \
                       liblcms2-dev \
                       libwebp-dev \
                       tcl8.6-dev \
                       tk8.6-dev \
                       python-tk \
                       build-essential \
                       libssl-dev \
                       libffi-dev \
                       libgeoip1 \
                       libgeoip-dev \
                       geoip-bin \
                       nodejs \
                       npm \
                       nginx \
                       supervisor \
                       wget \
                       mysql-client-5.5 \
                       git
RUN apt-get install -y python-virtualenv \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g stylus
RUN wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
RUN gunzip GeoLiteCity.dat.gz
RUN mkdir /usr/local/share/GeoIP
RUN mv GeoLiteCity.dat /usr/local/share/GeoIP/
COPY GeoIP2-City_20160726.tar.gz /GeoIP2-City_20160726.tar.gz
RUN tar -xzvf GeoIP2-City_20160726.tar.gz
RUN mkdir /usr/local/share/GeoIP2
RUN mv GeoIP2-City_20160726/GeoIP2-City.mmdb /usr/local/share/GeoIP2/

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install coverage==4.0.3
RUN pip install -U pip
