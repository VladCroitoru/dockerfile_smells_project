FROM ubuntu:14.04

MAINTAINER Krzysztof Pająk <kpajak@gmail.com>

RUN apt-get update && apt-get install -y \
  wget \
  curl \
  vim \
  git \
  nginx \
  telnet \
  htop \
  php5-curl \
  php5-cli \
  php5-fpm \
  php5-mongo \
  php5-xdebug

# Virtual host configuration
ADD symfony-vhost.conf /etc/nginx/sites-enabled/default

# Change php.ini
RUN echo "xdebug.max_nesting_level = 500" >> /etc/php5/cli/php.ini

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install node.js
RUN cd /tmp \
  && wget http://nodejs.org/dist/v0.12.0/node-v0.12.0-linux-x64.tar.gz \
  && tar -xzf node-v0.12.0-linux-x64.tar.gz \
  && mv node-v0.12.0-linux-x64 /node \
  && cd /usr/local/bin \
  && ln -s /node/bin/* .

# Create user with sudo
RUN adduser --disabled-password --gecos '' symfony \
  && adduser symfony sudo \
  && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN usermod -a -G www-data symfony

# Boot script
ADD boot.sh /boot.sh
RUN chmod +x /boot.sh
RUN mkdir /data

USER symfony

WORKDIR /data

EXPOSE 80

CMD ["/boot.sh"]
