FROM debian:latest
MAINTAINER Alejandro Escanero Blanco <aescanero@gmail.com>

LABEL maintainer="Alejandro Escanero Blanco <aescanero@gmail.com>" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.version="0.2" \
      org.label-schema.name="Apache2/php7 on Debian OS" \
      org.label-schema.url="https://www.disasterproject.com" \
      org.label-schema.vcs-url="https://github.com/aescanero/dockerevents/docker-fusiondirectory-apache.git"


RUN echo "deb http://repos.fusiondirectory.org/debian-jessie jessie main" \
    > /etc/apt/sources.list.d/fusiondirectory-jessie.list \
  && apt-get update

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \
  supervisor apache2-bin libapache2-mod-php5 fusiondirectory 

RUN apt-cache search smarty &&\
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes \
  fusiondirectory-smarty3-acl-render wget unzip python-daemon dnsutils\
  && mkdir -p /data/pids && mkdir -p /data/logs \
  && cd /data && wget "https://downloads.sourceforge.net/project/cnmonitor/CN%3DMonitor/3.2.1/cnmonitor-3.2.1-1.zip" -O cnmonitor-3.2.1-1.zip \
  && unzip cnmonitor-3.2.1-1.zip && mv cnmonitor /usr/share/. && chown www-data /usr/share/cnmonitor/www -R \
  && cp /usr/share/cnmonitor/conf/httpd/cnmonitor.conf /etc/apache2/conf-enabled/. \
  && rm -rf /var/lib/apt/lists/* 

ADD etc/fusiondirectory/fusiondirectory.conf /etc/fusiondirectory/fusiondirectory.conf
ADD etc/supervisord-fd2.conf /etc/supervisord-fd.conf
ADD apps/watcher/watcher_fd.py /usr/local/sbin/watcher_fd.py
ADD etc/cnmonitor/config.xml /usr/share/cnmonitor/config/config.xml

WORKDIR /data
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord-fd.conf"]
