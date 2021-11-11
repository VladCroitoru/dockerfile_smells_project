# Copyright 2016  Martin Scharm
#
# This file is part of TEXPILE.
# <https://github.com/binfalse/TEXPILE>
#
# TEXPILE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# TEXPILE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# TEXPILE. If not, see <http://www.gnu.org/licenses/>.



# let's use an apache+php image as a base
FROM php:apache

# see http://binfalse.de/contact/ if you want to contact me
MAINTAINER martin scharm


# install texlive, pygments (source code highlighting) and some zip dependencies
RUN apt-get clean && \
    apt-get -y update && \
    apt-get install --no-install-recommends -y \
        texlive-full \
        python-pygments \
        zlib1g-dev \
        libzip-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install zip support for php
RUN docker-php-ext-install -j$(nproc) zip

# enable the rewrite module
RUN a2enmod rewrite

# copy some php config -- we'd like to upload files bigger than default
COPY texpile/php.ini /usr/local/etc/php/

# copy the actual script into the image
COPY texpile/index.php /var/www/html/

# copy the .htaccess file into the image
# the .htaccess will map everything to the index.php script
# that's especially necessary for /heartbeat
COPY texpile/.htaccess /var/www/html/
