FROM cloutainer/k8s-jenkins-slave-base:v21

#
# BASE PACKAGES
#
RUN apt-get -qqy update \
    && apt-get -qqy --no-install-recommends install \
    g++ \
    build-essential \
    php7.0 \
    php7.0-cli \
    php7.0-common \
    php7.0-curl \
    php7.0-dev \
    php7.0-gd \
    php7.0-gmp \
    php7.0-json \
    php7.0-ldap \
    php7.0-mysql \
    php7.0-odbc \
    php7.0-opcache \
    php7.0-pgsql \
    php7.0-pspell \
    php7.0-readline \
    php7.0-recode \
    php7.0-sqlite3 \
    php7.0-tidy \
    php7.0-xml \
    php7.0-xmlrpc \
    php7.0-bcmath \
    php7.0-bz2 \
    php7.0-enchant \
    php7.0-imap \
    php7.0-interbase \
    php7.0-intl \
    php7.0-mbstring \
    php7.0-mcrypt \
    php7.0-phpdbg \
    php7.0-soap \
    php7.0-sybase \
    php7.0-xsl \
    php7.0-zip \
    php7.0-dba && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#
# COMPOSER
#
RUN curl -jkSL -o /tmp/composer-setup.php https://getcomposer.org/installer && \
    cd /tmp && php composer-setup.php && \
    mv composer.phar /usr/local/bin/composer


#
# INSTALL AND CONFIGURE
#
COPY docker-entrypoint-hook.sh /opt/docker-entrypoint-hook.sh
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint-hook.sh

#
# RUN
#
USER jenkins
