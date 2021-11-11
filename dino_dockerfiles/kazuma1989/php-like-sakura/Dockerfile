FROM debian:wheezy
MAINTAINER kazuma1989

# Install tools
RUN apt-get update \
    && apt-get install -y \
        apache2 \
        apache2-suexec-custom \
        curl \
        php5-cgi \
        php5-curl \
        php5-gd \
        php5-imagick \
        php5-mysql \
        unzip \
    && apt-get clean

# Activate Apache modules
RUN a2enmod \
        actions \
        cgid \
        rewrite \
        suexec

# Add Apache and PHP configs
COPY conf.d/user-home       /etc/apache2/conf.d/user-home
COPY conf.d/php5-cgi        /etc/apache2/conf.d/php5-cgi
COPY conf.d/www-data        /etc/apache2/suexec/www-data
COPY conf.d/timezone.ini    /etc/php5/cgi/conf.d/timezone.ini

# Create a user and document root instead of the default site
RUN a2dissite default
COPY scripts/add-user.sh /tmp/add-user.sh
RUN sh -x /tmp/add-user.sh web

# Start Apache foreground on debug mode
ENTRYPOINT ["apachectl", "-k", "start", "-DFOREGROUND"]
CMD ["-e", "debug"]

# Apache endpoint
EXPOSE 80
