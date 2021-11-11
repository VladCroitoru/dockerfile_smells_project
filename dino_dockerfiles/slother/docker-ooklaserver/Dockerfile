############################################################
# Dockerfile for Ookla Host Server
############################################################

FROM debian:jessie

# File Author / Maintainer
MAINTAINER Bartlomiej Przytarski <b.przytarski@gmail.com>
WORKDIR /data


RUN groupadd -r speedtest && useradd -r -g speedtest speedtest

RUN apt-get update && apt-get install -y \
    wget \
    apache2 \
    unzip \
    libapache2-mod-php5 \
    && rm -rf /var/lib/apt/lists/*

### Install Ookla Legacy Server
RUN wget http://cdn.speedtest.speedtest.net/http_legacy_fallback.zip && \
    unzip http_legacy_fallback.zip -d /var/www/html/ && \
    rm http_legacy_fallback.zip

### Install Ooklaserver
RUN wget http://install.speedtest.net/ooklaserver/ooklaserver.sh && \
    chmod a+x ooklaserver.sh && \
    ./ooklaserver.sh install -f

RUN chown -R speedtest:speedtest /data
RUN echo "" > /var/www/html/index.html

ADD crossdomain.xml /var/www/html
ADD startup.sh /usr/bin/startup.sh

ENTRYPOINT ["/bin/bash", "/usr/bin/startup.sh"]


EXPOSE 8080 80 5060
