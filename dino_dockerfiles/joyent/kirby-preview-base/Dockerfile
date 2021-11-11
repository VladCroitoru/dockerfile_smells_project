FROM php:5.6-apache

# Allow rewrites in Apache httpd
RUN a2enmod rewrite

# Get some packages, especially Git, but also some convenience items
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        git \
        less \
        vim \
    && rm -rf /var/lib/apt/lists/*

# Add Kirby base
COPY . /var/www/html/
