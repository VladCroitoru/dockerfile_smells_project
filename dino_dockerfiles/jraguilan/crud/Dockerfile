FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /tmp
# Install utils
RUN \
  apt-get update && \
  apt-get -y install wget \
                curl \
                apt-utils \
                ssmtp \
                xz-utils \
                libxrender-dev \
                git && \

# Configure git
  git config --global url."https://".insteadOf git:// && \

# Configure Dotdeb sources
  wget -O - http://www.dotdeb.org/dotdeb.gpg | apt-key add - && \
  echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list && \
  echo "\ndeb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.list && \
  apt-get update && \
  apt-get install -y php7.0-fpm \
                php7.0 \
                php7.0-pgsql 

FROM php:7.0-fpm

#install dependencies
RUN apt-get update -y && apt-get install -y openssl zip unzip git postgresql postgresql-contrib
RUN echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list
RUN apt-get update && DEBIAN_FRONTEND=noninteractive
#RUN apt-get install -y php7.0-pgsql
#RUN apt-get install -y libpcre3-dev

# Install Postgre PDO
#RUN apt-get install -y libpq-dev \
 #  && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
 #  && docker-php-ext-install pdo pdo_pgsql pgsql mbstring

FROM php:5.6-apache

RUN apt-get update && apt-get install -y libpq-dev && docker-php-ext-install pdo pdo_pgsql 

#install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN cd /home && \
   mkdir renzel
WORKDIR /home/renzel/
COPY . /home/renzel
#RUN composer install

#run app using port 9999
CMD php artisan serve --host=0.0.0.0 --port=9999
EXPOSE 9999