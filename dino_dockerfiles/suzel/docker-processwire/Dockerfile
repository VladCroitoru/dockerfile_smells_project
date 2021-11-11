FROM ubuntu:16.04
MAINTAINER Sukru Uzel <sukru.uzel@gmail.com>

# Packages installation
RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y \
    git \
    apache2 \
    libapache2-mod-php7.0 \
    php7.0 \
    php7.0-cli \
    php7.0-gd \
    php7.0-json \
    php7.0-ldap \
    php7.0-mbstring \
    php7.0-mysql \
    php7.0-xml \
    php7.0-xsl \
    php7.0-zip \
    php7.0-soap

# Update the default apache site with the config we created.
COPY config/apache/default.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Update php.ini
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g' /etc/php/7.0/apache2/php.ini
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g' /etc/php/7.0/cli/php.ini

# Install ProcessWire
RUN git clone git://github.com/processwire/processwire.git -b master /var/www/pw
RUN chown -R www-data:www-data /var/www/pw

# Expose
EXPOSE 80

# Volume
VOLUME ["/var/www/pw"]

# Clean
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/pw/.git

# Init
ADD scripts/init.sh /init.sh
RUN chmod +x /init.sh
CMD ["/init.sh"]
