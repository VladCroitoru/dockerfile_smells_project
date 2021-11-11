FROM wordpress:php7.1

RUN set -x \
	&& apt-get update \
	&& apt-get install -y libldap2-dev mcrypt libmcrypt-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
	&& docker-php-ext-install ldap mcrypt \
	&& apt-get purge -y --auto-remove libldap2-dev \
	&& a2enmod ldap \
	&& a2enmod authnz_ldap \
	&& echo -e "\nTLS_REQCERT never\n" >> /etc/ldap/ldap.conf

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=60'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/opcache-recommended.ini

# increase upload size
# see http://php.net/manual/en/ini.core.php
RUN { \
    echo "upload_max_filesize = 25M"; \
    echo "post_max_size = 50M"; \
  } > /usr/local/etc/php/conf.d/uploads.ini

# Iron the security of the Docker
RUN { \
    echo "expose_php = Off"; \
    echo "display_startup_errors = off"; \
    echo "display_errors = off"; \
    echo "html_errors = off"; \
    echo "log_errors = on"; \
    echo "error_log = /dev/stderr"; \
    echo "ignore_repeated_errors = off"; \
    echo "ignore_repeated_source = off"; \
    echo "report_memleaks = on"; \
    echo "track_errors = on"; \
    echo "docref_root = 0"; \
    echo "docref_ext = 0"; \
    echo "error_reporting = -1"; \
    echo "log_errors_max_len = 0"; \
  } > /usr/local/etc/php/conf.d/security.ini

RUN { \
    echo "ServerSignature Off"; \
    echo "ServerTokens Prod"; \
    echo "TraceEnable off"; \
  } >> /etc/apache2/apache2.conf
