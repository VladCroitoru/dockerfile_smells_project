# Pull base image.
FROM composer
MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

# Install rsync for deployment
RUN apk --no-cache add openssh-client rsync openssl zlib-dev icu-dev libxml2-dev g++ autoconf openssl-dev make pcre-dev libpng-dev libmcrypt-dev

RUN docker-php-ext-configure intl

#install mysql pdo
RUN docker-php-ext-install pdo pdo_mysql bcmath soap pcntl gd mcrypt exif

#install mongodb php extension
RUN pecl install mongodb-1.2.9 \
  && docker-php-ext-enable mongodb

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
