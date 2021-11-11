FROM psycho0verload/armv7hf-debian-qemu
MAINTAINER Psycho0verload
ENV DEBIAN_FRONTEND noninteractive
RUN ["cross-build-start"]
RUN echo 'deb http://deb.debian.org/debian stretch-backports main' > /etc/apt/sources.list.d/backports.list && \
    apt update && \
    apt upgrade -qy && \
    apt-get autoremove && \
    apt-get clean && \
    apt install -qy \
    php7.0 \
    php7.0-curl \
    php7.0-gd \
    php7.0-fpm \
    php7.0-cli \
    php7.0-opcache \
    php7.0-mbstring \
    php7.0-xml \
    php7.0-zip \
    nginx \
    openssl \
    certbot
RUN [ "cross-build-end" ]
EXPOSE 80 443
