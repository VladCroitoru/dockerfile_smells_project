FROM php:8.0.11-fpm

RUN apt-get update && apt-get install -y \
git \
curl \
zip \
unzip

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www