FROM php:apache

MAINTAINER Pongpat Poapetch <p.poapetch@gmail.com>

# Insert this line before "RUN apt-get update" to dynamically
# replace httpredir.debian.org with a single working domain
# in attempt to "prevent" the "Error reading from server" error.
# RUN sed -i "s/httpredir.debian.org/mirrors.tuna.tsinghua.edu.cn/" /etc/apt/sources.list

# Update library
RUN apt-get -y update

# Install require packages
RUN apt-get install -y libcurl4-gnutls-dev php5-curl php5-dev php5-mysql vim wget unzip

# Install mongodb extension
RUN pecl install mongodb

# Install php-extension (.so) from helper binary
RUN docker-php-ext-install curl && \
    docker-php-ext-install mbstring && \
    docker-php-ext-install tokenizer && \
    docker-php-ext-install pdo && \
    docker-php-ext-install pdo_mysql && \
    docker-php-ext-install mysqli && \
    docker-php-ext-enable mongodb

# Enable mod rewrite and ssl
RUN a2enmod rewrite && a2enmod ssl

# Copy public_html
COPY public_html /var/www/html

# mod user www-data to id 1000 (fix bug on mac osx)
RUN usermod -u 1000 www-data

# set terminal in container to xterm
RUN echo "export TERM=xterm" >> /root/.bashrc

# expose port 80
EXPOSE 80
