FROM php:7-apache
MAINTAINER Camille Baronnet <docker@camillebaronnet.fr>

ENV VERSION 2.3
ENV VERSIONFULL 2.3.7
ENV TERM xterm

ENV ZPUSH_URL zpush_default
ENV ZIMBRA_HOST localhost

RUN apt-get update && apt-get install -y wget

RUN cd /var/www/html && \
	wget -O - "http://download.z-push.org/final/${VERSION}/z-push-${VERSIONFULL}.tar.gz" | tar --strip-components=1 -x -z && ls -lah
RUN mkdir /tmp/zimbra && cd /tmp/zimbra && \
	wget -O - "http://downloads.sourceforge.net/project/zimbrabackend/Release66/zimbra66.tgz?use_mirror=freefr" | tar --strip-components=1 -x -z
RUN	mv /tmp/zimbra /var/www/html/backend/zimbra

RUN mkdir /var/log/z-push/ && mkdir /var/lib/z-push
RUN chmod -R 777 /var/log/z-push && chmod -R 777 /var/lib/z-push

RUN sed -i "s/#ZPUSH_HOST#/$ZPUSH_URL/" /var/www/html/config.php
RUN sed -i "s/#ZIMBRA_HOST#/$ZIMBRA_HOST/" /var/www/html/config.php


COPY autodiscover/ /var/www/html/autodiscover/
COPY config.php /var/www/html/config.php
COPY default.vhost /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod alias rewrite

COPY ./startup.sh /root/startup.sh
CMD ["/bin/bash", "/root/startup.sh"]
