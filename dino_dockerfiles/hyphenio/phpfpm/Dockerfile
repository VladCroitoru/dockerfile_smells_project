FROM ubuntu:16.04
MAINTAINER Hyphen IO <services@hyphenio.com.au>

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >> /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/nginx/stable/ubuntu xenial main " >> /etc/apt/sources.list

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com --recv 14AA40EC0831756756D7F66C4F4EA0AAE5267A6C
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com --recv 8B3981E7A6852F782CC4951600A6F0A3C300EE8C

RUN apt-key update
RUN apt-get update
RUN apt-get -y dist-upgrade

RUN apt-get -y install \
  php \
  php-fpm \
  php-tidy \
  php-xml \
  php-bcmath \
  php-gd \
  php-mbstring \
  php-curl \
  php-mysql \
  php-zip \
  php-mcrypt \
  php-imagick
RUN apt-get -y clean
RUN apt-get -y autoclean
RUN apt-get -y autoremove

WORKDIR /opt/app
RUN echo "#!/bin/bash" > /bin/deploy.sh
RUN echo "/usr/sbin/php-fpm7.1 --nodaemonize -y /opt/app/server/fpm/php-fpm.conf -c /opt/app/server/php" >> /bin/deploy.sh
RUN chmod 777 /bin/deploy.sh

CMD ["/bin/deploy.sh"]
