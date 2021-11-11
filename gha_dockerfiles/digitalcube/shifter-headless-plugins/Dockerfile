FROM php:7.4-cli-buster as composer
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update  --allow-releaseinfo-change --allow-insecure-repositories \
  && apt-get upgrade -y && apt-get install -y unzip git

WORKDIR /tmp
# Note: pinning install > php composer-setup.php --version=1.5.6

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php composer-setup.php --version=1.10.16 \
  && php -r "unlink('composer-setup.php');" \
  && install -m 0755 ./composer.phar /usr/local/bin/composer

RUN /usr/local/bin/composer --version

COPY build /srv/build

WORKDIR /srv/build/lite
RUN composer install

WORKDIR /srv/build/full
RUN composer install


FROM busybox:latest
ARG STAGE=full
COPY --from=composer /srv/build/${STAGE}/plugins /srv/plugins
VOLUME /srv/plugins
ENTRYPOINT [ "/bin/true" ]
