# Dockerfile to Build flyspray on Apache
FROM php:5.6-apache
MAINTAINER John Gratton <jgratton@gmail.com>

# Set Date of Refresh if you need to rebuild the image
# Format: YYYY-MM-DD
ENV REFRESHED_AT 2015-02-08

# Install Git
RUN apt-get update && \
    apt-get install -y git zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Install mod_rewrite for Apache
RUN a2enmod rewrite

# Install PHP Extensions
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install zip

# Remove html directory
RUN rm -rf /var/www/html

# Set Working Directory
WORKDIR /tmp

# Download Latest FlySpray
RUN git clone https://github.com/Flyspray/flyspray.git

# Install Composer
WORKDIR /tmp/flyspray
RUN curl -sS https://getcomposer.org/installer | php
RUN php composer.phar install

# Add the flyspray initialization script
ADD defaults/start.bash /initialize-flyspray

# Set Mountable Volume
VOLUME ["/var/www"]

# Run the initialization script upon container creation
CMD ["bash", "/initialize-flyspray"]