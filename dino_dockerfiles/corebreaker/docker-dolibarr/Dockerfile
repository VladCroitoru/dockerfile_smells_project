FROM ubuntu:xenial
MAINTAINER Frédéric Meyer <frederic.meyer.77@gmail.com>

RUN set -x ; \
    locale-gen fr_FR.UTF-8 fr_FR@euro && \
    DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        dialog \
        apt-utils \
        libterm-ui-perl && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        apache2 \
        apache2-data \
        apache2-utils \
        dolibarr \
        mysql-common \
        mysql-server \
        dbconfig-mysql && \
    cat /usr/share/dolibarr/htdocs/install/mysql/tables/llx_product.sql |sed 's/^  virtual\([ \t]\)/  `virtual`\1/' >/.llx_product.sql && \
    mv /.llx_product.sql /usr/share/dolibarr/htdocs/install/mysql/tables/llx_product.sql && \
    service mysql start && \
    ( \
        echo 'CREATE DATABASE `dolibarr` CHARACTER SET utf8;' ; \
        echo "GRANT USAGE ON *.* to dolibarr@localhost identified by 'dolibarr';" ;  \
        echo "GRANT ALL PRIVILEGES ON dolibarr.* to dolibarr@localhost identified by 'dolibarr';" ; \
        echo "FLUSH PRIVILEGES;" ; \
    ) |mysql && \
    service mysql stop && \
    rm -f /etc/apache2/conf-enabled/dolibarr.conf && \
    ( \
        echo '<VirtualHost *:80>' ; \
        echo '	ServerAdmin webmaster@localhost' ; \
        echo '	DocumentRoot /usr/share/dolibarr/htdocs' ; \
        echo '' ; \
        echo '    <Directory /usr/share/dolibarr/htdocs>' ; \
        echo '        <IfVersion >= 2.3>' ; \
        echo '        Require all granted' ; \
        echo '        </IfVersion>' ; \
        echo '        <IfVersion < 2.3>' ; \
        echo '        Order deny,allow' ; \
        echo '        Allow from all' ; \
        echo '        </IfVersion>' ; \
        echo '' ; \
        echo '        DirectoryIndex index.php' ; \
        echo '        Options +FollowSymLinks +Indexes' ; \
        echo '' ; \
        echo '        ErrorDocument 401 /dolibarr/public/error-401.php' ; \
        echo '        ErrorDocument 404 /dolibarr/public/error-404.php' ; \
        echo '' ; \
        echo '        <IfModule mod_php.c>' ; \
        echo '          php_flag magic_quotes_gpc Off' ; \
        echo '          php_flag register_globals Off' ; \
        echo '        </IfModule>' ; \
        echo '    </Directory>' ; \
        echo '' ; \
        echo '	ErrorLog ${APACHE_LOG_DIR}/error.log' ; \
        echo '	CustomLog ${APACHE_LOG_DIR}/access.log combined' ; \
        echo '</VirtualHost>' ; \
    ) >/etc/apache2/sites-available/000-default.conf && \
    ( \
        echo "#! /bin/sh" ; \
        echo "case $1 in" ; \
        echo "    www) apachectl -DFOREGROUND ;;" ; \
        echo "    db) /usr/sbin/mysql ;;" ; \
        echo "esac" ; \
    ) >/dolibarr-frontend.sh && \
    chmod +x /dolibarr-frontend.sh

EXPOSE 80

ENTRYPOINT ["/dolibarr-frontend.sh"] 

