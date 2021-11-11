FROM webdevops/php-nginx:alpine

ARG GRAV_VERSION=1.6.9

#RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update
RUN apk add --update \
    git \
    yaml-dev \
    memcached \
    php7-dev \
    g++ \
    make

RUN rm -rf /var/cache/apk/*

# Install YAML extension
RUN pecl install yaml-2.0.2
RUN echo "extension=yaml.so" >> /opt/docker/etc/php/php.ini

USER application

RUN wget -P /tmp/ https://github.com/getgrav/grav/releases/download/$GRAV_VERSION/grav-admin-v$GRAV_VERSION.zip && \
    unzip /tmp/grav-admin-v$GRAV_VERSION.zip -d /tmp/ && \
    rm /tmp/grav-admin-v$GRAV_VERSION.zip && \
    cd /tmp/grav-admin && \
    bin/gpm install -f -y admin

RUN mv -v /tmp/grav-admin/* /app/

COPY ./grav.vhost.conf /opt/docker/etc/nginx/vhost.conf
