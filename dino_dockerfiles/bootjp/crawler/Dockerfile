FROM fedora:latest

MAINTAINER oh@bootjp.me

ADD ./ /app/

RUN dnf install -y php-cli php-mbstring git  && dnf clean all
RUN cd /app && curl -sS https://getcomposer.org/installer | /usr/bin/php && /usr/bin/php composer.phar install
