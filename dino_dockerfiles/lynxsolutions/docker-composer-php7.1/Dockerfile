# Pull base image.
FROM composer/composer
MAINTAINER Lorand David <lorand.david@lynxsolutions.eu>

# Latest Git version
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list

# Install rsync for deployment
RUN apt-get update  \
  && apt-get install -y php7.1 openssh-client rsync libssl-dev zlib1g-dev libicu-dev g++ git php7.1-xml php7.1-gd php7.1-mbstring php7.1-curl php7.1-sqlite php7.1-ldap \
  && rm -r /var/lib/apt/lists/*

RUN docker-php-ext-configure intl

#install mysql pdo
RUN docker-php-ext-install pdo pdo_mysql bcmath soap ldap

#install mongodb php extension
RUN pecl install mongodb-1.2.9 \
  && docker-php-ext-enable mongodb

#set correct path to php 7.1
RUN rm /usr/local/bin/php && ln -s /usr/bin/php7.1 /usr/local/bin/php

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
