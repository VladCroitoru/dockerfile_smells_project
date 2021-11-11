FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -yqq ca-certificates apache2 php5 php5-cli php5-gd php-pear php5-dev php5-mysql php5-json php-services-json git && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 https://github.com/sipcapture/homer/ /homer

RUN cp -R /homer/webhomer /var/www/html/
RUN chmod -R 0777 /var/www/html/webhomer/tmp

COPY configuration.php /var/www/html/webhomer/configuration.php
COPY preferences.php /var/www/html/webhomer/preferences.php
COPY vhost.conf /etc/httpd/conf.d/000-homer.conf
COPY run.sh /run.sh

ENTRYPOINT [ "/run.sh" ]
