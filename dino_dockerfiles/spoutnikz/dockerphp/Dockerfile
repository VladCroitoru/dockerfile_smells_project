FROM ubuntu:16.04

MAINTAINER Cédric Billiet <cedricbilliet@gmail.com>
RUN apt-get -y update && apt-get install -y php7.0 php7.0-dev php7.0-curl php7.0-gd php7.0-json php7.0-mcrypt php7.0-mbstring php-gettext php7.0-mysql php7.0-tidy php7.0-xml php-redis php-soap php-zip
RUN apt-get install -y php-xdebug wget
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer -O - -q | php -- --quiet
RUN mv composer.phar /usr/local/bin/composer