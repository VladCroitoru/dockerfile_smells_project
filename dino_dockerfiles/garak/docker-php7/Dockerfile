FROM ubuntu:20.04

MAINTAINER Massimiliano Arione <garakkio@gmail.com>

# Set correct environment variables
ENV HOME /root
ENV LANG it_IT.UTF-8
ENV LC_ALL it_IT.UTF-8

ARG DEBIAN_FRONTEND=noninteractive

RUN \
    apt-get update && apt-get install -y --no-install-recommends locales && locale-gen it_IT.UTF-8

RUN \
    apt-get update && apt-get install -y --no-install-recommends software-properties-common && \
    apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    unzip \
    mcrypt \
    wget \
    openssl \
    ssh \
    locales \
    libonig-dev \
    && rm -r /var/lib/apt/lists/* \
    && apt-get --purge autoremove -y

# OpenSSL
RUN mkdir -p /usr/local/openssl/include/openssl/ && \
    ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \
    mkdir -p /usr/local/openssl/lib/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/

# PHP Extensions
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y -qq --no-install-recommends php7.4-zip php7.4-xml php7.4-mbstring php7.4-curl php7.4-json php7.4-mysql php7.4-tokenizer php7.4-cli php7.4-intl

# Libraries needed for wkhtmltopdf
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends libxext6 libxrender1 libfontconfig1 libjpeg62

# Time Zone
RUN echo "date.timezone=Europe/Rome" > /etc/php/7.4/cli/conf.d/date_timezone.ini

VOLUME /root/composer

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Goto temporary directory.
WORKDIR /tmp

RUN apt-get clean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

