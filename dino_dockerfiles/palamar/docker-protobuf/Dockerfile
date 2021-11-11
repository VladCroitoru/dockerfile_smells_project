FROM php:5.6-cli-alpine as compiler

RUN apk update
RUN apk add protobuf 
RUN pecl channel-update pecl.php.net
RUN pear install Console_CommandLine
RUN pear channel-discover pear.pollinimini.net
RUN pear install drslump/Protobuf-beta
RUN mkdir -p /tmp/src
RUN echo 'error_reporting = E_ALL & ~E_WARNING;' > /usr/local/etc/php/php.ini
WORKDIR /tmp/src
