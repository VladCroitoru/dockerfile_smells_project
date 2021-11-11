# Pull base image.
FROM composer:1.4

MAINTAINER Nimrod Nagy <nimrod.nagy@lynxsolutions.eu>

RUN apk --no-cache add rsync openssh-client icu-dev libxml2-dev

RUN docker-php-ext-configure intl

#install mysql pdo
RUN docker-php-ext-install pdo pdo_mysql bcmath soap

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
