FROM php:7-apache

MAINTAINER Michael Kenney <mkenney@webbedlam.com>

RUN set -x \

    # System update
    && apt-get -qqy update \

    && apt-get install -qqy \
        less \
        sendmail \
        vim \
    && apt-get clean && rm -r /var/lib/apt/lists/* \

    # Install PHP modules
    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_mysql \

    # Allow Header overrides in .htaccess files
    && a2enmod headers \

    # fix the issue caused by upstream modifications to 000-default.conf
    && a2dissite 000-default \

    # Configure logging
    && rm /var/log/apache2/access.log && ln -s /dev/stdout /var/log/apache2/access.log \
    && rm /var/log/apache2/error.log && ln -s /dev/stdout /var/log/apache2/error.log \
    && ln -s /etc/apache2/mods-available/macro.load /etc/apache2/mods-enabled/macro.load

# Apache configuration defaults
ENV DOCUMENTROOT_PATH /var/www/html/documentroot
ENV VIRTUAL_PORT 80
ENV VIRTUAL_HOST example.com

# Configure terminal
ENV TERM xterm
COPY container/root/ /root/

# Configure Apache & PHP
#COPY container/etc/apache2/sites-enabled/vhost.conf /etc/apache2/sites-enabled/
COPY container/etc/apache2/ports.conf /etc/apache2/ports.conf
COPY container/etc/php.ini /usr/local/etc/php/

# Fix the Apache init script to execute apache in the foreground. A recent
# update broke the previous entrypoint command.
COPY container/etc/init.d/apache2 /etc/init.d/apache2

# Use a custom entrypoint script to configure port listeners
COPY container/entrypoint.sh /entrypoint.sh

WORKDIR /var/www/html

# Make sure it all fires off
RUN chmod +x /entrypoint.sh \
    && chmod +x /etc/init.d/apache2

EXPOSE 80

# Use a custom entrypoint script to configure port listeners and start
# apache in the forground with the modified init.d script
ENTRYPOINT /entrypoint.sh

