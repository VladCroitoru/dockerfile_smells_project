FROM debian:jessie

################################################################################
# Installation de wget
################################################################################

RUN \
    apt-get -qq update --fix-missing && \
    apt-get -qq install -y \
    wget

################################################################################
# Mise en place de DotDeb
################################################################################

RUN \
    echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.org.list && \
    wget http://www.dotdeb.org/dotdeb.gpg -O dotdeb.gpg && \
    apt-key add dotdeb.gpg

################################################################################
# Installation des Libs Apache / PHP7 / Extensions de PHP
################################################################################

RUN \
    apt-get -qq update --fix-missing && \
    apt-get -qq install -y \
        php7.0 \
        apache2 \
        libapache2-mod-php7.0 \
        php7.0-mysql \
        php7.0-gd \
        php7.0-imagick \
        php7.0-dev \
        php7.0-curl \
        php7.0-opcache \
        php7.0-cli \
        php7.0-intl \
        php7.0-json \
        php7.0-mcrypt \
        php7.0-common \
        php7.0-apcu-bc \
        php7.0-mbstring \
        php7.0-zip \
        php7.0-xml

################################################################################
# Paramétrage de Apache / Inspiré de l'image php:7.0-latest
################################################################################

ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars

# Activation des modules Apache
RUN \
    a2dismod mpm_event && \
    a2enmod mpm_prefork && \
    a2enmod php7.0 && \
    a2enmod rewrite && \
    a2enmod headers

# logs should go to stdout / stderr
RUN \
    set -ex && \
    . "$APACHE_ENVVARS" && \
    ln -sfT /dev/stderr "$APACHE_LOG_DIR/error.log" && \
    ln -sfT /dev/stdout "$APACHE_LOG_DIR/access.log" && \
    ln -sfT /dev/stdout "$APACHE_LOG_DIR/other_vhosts_access.log"

################################################################################
# Installation des dépendances relatives au projet selfimmo
################################################################################

RUN \
    apt-get -qq update --fix-missing && \
    apt-get -qq install -y build-essential \
        libxrender-dev \
        zip \
        unzip \
        vim \
        curl \
        xvfb \
        wkhtmltopdf

WORKDIR /var/www/html

################################################################################
# Installation de composer
################################################################################

# /!\ le hash du fichier composer_install.sh impose une version particulière

RUN \
    wget https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer -O - -q | php -- --quiet

################################################################################
# Installation des dépendances relatives à l'optimisation des images par liip
################################################################################

RUN \
    apt-get -qq install -y jpegoptim optipng

################################################################################
# Suppression des fichiers temporaires.
################################################################################

RUN \
    apt-get -qq clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

################################################################################
# Autorisations sur les répertoires caches et log.
################################################################################

RUN \
    mkdir -p /var/www/html/app/cache && \
    mkdir -p /var/www/html/app/logs && \
    chown -R www-data:www-data /var/www/html/app/cache && \
    chown -R www-data:www-data /var/www/html/app/logs

################################################################################
# Autorisations sur le répertoire composer
################################################################################

RUN \
    mkdir -p /var/www/.composer && \
    chown -R www-data:www-data /var/www/.composer

################################################################################
# Lancement d'apache en tache de fond
################################################################################

COPY apache2-foreground /usr/local/bin/
EXPOSE 80
CMD ["apache2-foreground"]

################################################################################
# Configuration de wkhtmltopdf
################################################################################

COPY wkhtmltopdf.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/wkhtmltopdf.sh
