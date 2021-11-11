FROM php:7.2.3-cli

RUN apt update && apt upgrade -y git zip wget

COPY ./phpadr /

RUN mkdir ./src-app
RUN mkdir ./workspace

WORKDIR /src-app
# https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer -O - -q | php -- --quiet --install-dir=/usr/local/bin --filename=composer
RUN composer require globtec/phpadr

WORKDIR /workspace

ENTRYPOINT ["/phpadr"]