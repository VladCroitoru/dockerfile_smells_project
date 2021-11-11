FROM debian:jessie

ENV NEXTCLOUD_VERSION 13.0.1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q -y update \
 && apt-get -q -y install --no-install-recommends cron \
 && apt-get -q -y install apache2 \
                          openssl \
                          wget \
                          curl \
                          bzip2 \
                          php5 \
                          php5-imap \
                          php5-curl \
                          php5-gd \
                          php5-gmp \
                          php5-intl \
                          php5-ldap \
                          php5-mysql \
                          php5-pgsql \
                          php5-sqlite \
                          php5-mcrypt \
                          mysql-client \
                          sendmail \
                          smbclient \
 && apt-get -q -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 \
 && sed -i 's/^ServerSignature/#ServerSignature/g' /etc/apache2/conf-enabled/security.conf \
 && sed -i 's/^ServerTokens/#ServerTokens/g' /etc/apache2/conf-enabled/security.conf \
 && echo "ServerSignature Off" >> /etc/apache2/conf-enabled/security.conf \
 && echo "ServerTokens Prod" >> /etc/apache2/conf-enabled/security.conf \
 && echo "SSLProtocol ALL -SSLv2 -SSLv3" >> /etc/apache2/apache2.conf \
 && a2enmod ssl \
 && a2enmod headers \
 \
 && mkdir -p /etc/apache2/external \
 && rm -rf /var/www/html/* \
 && rm -rf /etc/apache2/sites-enabled/* \
 \
 && curl -fsSL -o nextcloud.tar.bz2 "https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" \
 && curl -fsSL -o nextcloud.tar.bz2.asc "https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.asc" \
 && export GNUPGHOME="$(mktemp -d)" \
 && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 28806A878AE423A28372792ED75899B9A724937A \
 && gpg --batch --verify nextcloud.tar.bz2.asc nextcloud.tar.bz2 \
 && rm -r "$GNUPGHOME" nextcloud.tar.bz2.asc \
 && cd /var/www/ \
 && tar xvjf /nextcloud.tar.bz2 \
 && rm /nextcloud.tar.bz2 \
 && chmod a+x /var/www/nextcloud/occ \
 && mkdir -p /var/www/nextcloud/data \
 && cd - \
 \
 && mkdir -p /etc/apache2/ssl \
 \
 && a2enmod rewrite \
 && a2enmod env \
 && a2enmod dir \
 && a2enmod mime \
 \
 && echo "*/15  *  *  *  *	www-data	php -f /var/www/nextcloud/cron.php" >> /etc/crontab \
 \
 && sed -i 's/;default_charset = "UTF-8"/default_charset = "UTF-8"/g' /etc/php5/apache2/php.ini \
 && sed -i 's/memory_limit = 128M/memory_limit = 256M/g' /etc/php5/apache2/php.ini \
 \
 && sed -i 's/^post_max_size =.*/post_max_size = 0/g' /etc/php5/apache2/php.ini \
 && sed -i 's/^upload_max_filesize =.*/upload_max_filesize = 55G/g' /etc/php5/apache2/php.ini \
 && sed -i 's/^max_file_uploads =.*/max_file_uploads = 100/g' /etc/php5/apache2/php.ini \
 \
 && chown www-data:www-data -R /var/www/nextcloud/ \
 && chmod -R a+rw /var/www/nextcloud/data \
 && cp -a /var/www/nextcloud/data /var/www/nextcloud/data.bak \
 && cp -a /var/www/nextcloud/apps /var/www/nextcloud/apps.bak \
 && cp -a /var/www/nextcloud/config /var/www/nextcloud/config.bak

EXPOSE 443
VOLUME ["/var/www/nextcloud/data","/var/www/nextcloud/apps","/var/www/nextcloud/config"]

COPY sites-enabled /etc/apache2/sites-enabled

COPY scripts /usr/local/bin
HEALTHCHECK CMD ["docker-healthcheck.sh"]
ENTRYPOINT ["entrypoint.sh"]
