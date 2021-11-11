# Copyright (C) 2015, BMW Car IT GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

FROM php:5.6-apache
MAINTAINER David Brown <dmlb2000@gmail.com>

RUN apt-get update && \
    apt-get -y install ssl-cert libgmp-dev && \
    apt-get clean all && \
    a2enmod ssl && \
    a2ensite default-ssl && \
    sed -i 's|ErrorLog .*|ErrorLog /proc/self/fd/2|;s|CustomLog .*|CustomLog /proc/self/fd/1 combined|' /etc/apache2/sites-available/default-ssl.conf && \
    make-ssl-cert generate-default-snakeoil --force-overwrite && \
    ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && \
    for lib in /usr/lib/x86_64-linux-gnu/libgmp* ; do \
      ln -s $lib /usr/lib/$(basename $lib) ; \
    done && \
    docker-php-ext-install mbstring && \
    docker-php-ext-install bcmath && \
    docker-php-ext-install gmp

# install simpleid server
RUN mkdir -p /data/logs
RUN curl -L http://downloads.sourceforge.net/simpleid/simpleid-1.0.0.tar.gz | tar -C /data -xzf - && rm -rf /var/www/html/ && ln -s /data/simpleid/www /var/www/html
RUN chown www-data.www-data /data/logs /data/simpleid/store /data/simpleid/cache

EXPOSE 443

# configure simpleid server
COPY config.php /data/simpleid/www/config.php
VOLUME /data/simpleid/identities

