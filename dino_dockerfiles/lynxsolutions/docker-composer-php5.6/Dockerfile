# Pull base image.
FROM composer/composer:master-php5
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

# Latest Git version
RUN echo "deb http://ftp.us.debian.org/debian testing main contrib non-free" >> /etc/apt/sources.list

# Install rsync for deployment
RUN apt-get update \
  && apt-get install -y openssh-client rsync php-soap php5-gd zlib1g-dev libicu-dev g++ git \
  && rm -r /var/lib/apt/lists/*

#install mysql pdo
RUN docker-php-ext-install pdo pdo_mysql soap gd intl

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
