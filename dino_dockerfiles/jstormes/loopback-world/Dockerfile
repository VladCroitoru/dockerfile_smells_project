# This is a convenience container for local workstation development
#
# This is a Docker Anti-Pattern.  I am putting all the services into
# one container and I am doing it knowing that this is NOT the way
# you should do it.   That is just how I roll...
#
# Breaking the law, breaking the law ...
#
# This is intended for development but also allows less experienced
# system operators to deploy to system like QNAP NAS server as one
# container, without having to understand how to connect and
# maintain separate services.
#

FROM php:7-apache
MAINTAINER James Stormes <jstormes@stormes.net>


############################################################################
# Base requriments, this should be the simmiler between development, QA and
# produciton.
############################################################################


############################################################################

# Add Tini
ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini

# Add custom init script
ADD assets/scripts/init.sh /etc/init.sh
ADD assets/scripts/copy_sshkey.sh /root/.copy_sshkey.sh
ADD assets/scripts/bashrc.sh /root/.bashrc
RUN chmod a+x /etc/init.sh \
    && chmod a+x /root/.copy_sshkey.sh \
    && chmod a+x /root/.bashrc

ADD assets/ldap/debconfig-set-selections.txt /etc/ldap

RUN docker-php-ext-install pdo pdo_mysql mysqli \
    && a2enmod rewrite ssl \
    && apt-get update \
    && cat /etc/ldap/debconfig-set-selections.txt | debconf-set-selections \
    && rm /etc/ldap/debconfig-set-selections.txt \
    && apt-get install -y cron mariadb-server at redis-server slapd ldap-utils ldapscripts syslog-ng-core \
    && chmod +x /tini \
    && chmod +x /etc/init.sh \
    && rm -f /var/log/apache2/access.log \
    && rm -f /var/log/apache2/error.log \
    && rm -f /var/log/apache2/other_vhosts_access.log \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run your init under Tini
ENTRYPOINT ["/tini", "/etc/init.sh"]



# Install Linux tools, PHP Composer, PHP tools, XDebug, and Apache's vhost alias.
# Remove all Aapche enabled sites.
RUN apt-get update \
 && apt-get install -y net-tools curl wget git zip unzip zlib1g-dev libpng-dev mariadb-client \
    joe gnupg2 libldap2-dev inetutils-ping gettext ssl-cert \
 && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
 && docker-php-ext-install gd zip ldap gettext \
 && wget https://getcomposer.org/installer \
    && php installer \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require phpunit/phpunit \
       phpunit/dbunit \
       phing/phing \
       sebastian/phpcpd \
       phploc/phploc \
       phpmd/phpmd \
       squizlabs/php_codesniffer \
    && rm installer \
 && yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && yes '' | pecl install -f redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis \
 && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs build-essential \
    && npm -g install grunt-cli nano yarn \
    && echo '{ "allow_root": true }' > /root/.bowerrc \
 && a2enmod vhost_alias http2 headers \
 && rm -fr /etc/apache2/sites-enabled/* \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && /bin/bash -c "/usr/bin/mysqld_safe &" \
    && sleep 5 \
    && mysql -u root -pnaked -e "CREATE USER 'root'@'%' IDENTIFIED BY 'naked';" \
    && mysql -u root -pnaked -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;" \
    && mysql -u root -pnaked -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'naked' WITH GRANT OPTION;" \
    && sed -i '/bind-address/c\bind-address\t\t= 0.0.0.0' /etc/mysql/my.cnf \
    && sed -Ei "s/bind-address.*/bind-address=0.0.0.0/g" /etc/mysql/mariadb.conf.d/50-server.cnf \
 && chmod -R a+rw /var/log/apache2

# Apache config
ADD assets/apache2/sites/100-loopback-world-ssl.conf /etc/apache2/sites-enabled/
ADD assets/apache2/sites/100-loopback-world.conf /etc/apache2/sites-enabled/

# LDAP Config
ADD assets/ldap/ssl.ldif /etc/ldap/
ADD assets/ldap/ldap.conf /etc/ldap/

# CRON Config
ADD assets/cron/crontab /etc/

# Add certificates
ADD assets/ssl/certs/loopback.world.cert.pem /etc/ssl/certs/
ADD assets/ssl/certs/loopback.world.fullchain.pem /etc/ssl/certs/
ADD assets/ssl/private/loopback.world.privkey.pem /etc/ssl/private/


# Final adjustments to to image
RUN chown :ssl-cert /etc/ssl/private/loopback.world.privkey.pem \
 && chmod 640 /etc/ssl/private/loopback.world.privkey.pem \
 && usermod -aG ssl-cert openldap \
 && usermod -aG ssl-cert www-data \
 && /bin/bash -c "service slapd start" \
    && sleep 10 \
    && ldapmodify -H ldapi:// -Y EXTERNAL -f /etc/ldap/ssl.ldif


EXPOSE 443 80 3306

# Install custom .bashrc
ADD assets/scripts/bashrc.sh /root/.bashrc
RUN chmod u+x /root/.bashrc

# Add our script files so they can be found
ENV PATH /root/bin:~/.composer/vendor/bin:$PATH



RUN mkdir /var/tools \
 && git clone https://github.com/breisig/phpLDAPadmin.git /var/tools/phpLDAPadmin \
 && git clone https://github.com/erikdubbelboer/phpRedisAdmin.git /var/tools/phpRedisAdmin \
    && cd /var/tools/phpRedisAdmin \
    && composer -n --no-ansi --optimize-autoloader install \
 && git clone https://github.com/phpmyadmin/phpmyadmin.git /var/tools/phpmyadmin \
    && cd /var/tools/phpmyadmin \
    && composer -n --no-ansi --optimize-autoloader install \
    && mkdir tmp \
    && chmod a+rw tmp

ADD assets/tools/apache2/sites/ /etc/apache2/sites-enabled/
ADD assets/tools/apache2/tools.conf /etc/apache2/conf-enabled
ADD assets/tools/phpMyAdmin/config.inc.php /var/tools/phpmyadmin
ADD assets/tools/phpLDAPadmin/config.php /var/tools/phpLDAPadmin/config



# Varables to make LAMP development easer.
ENV XDEBUG_CONFIG remote_host=host.docker.internal remote_port=9000 remote_autostart=1
ENV MYSQL_PWD naked
ENV MYSQL_USER root
ENV MYSQL_HOST localhost




