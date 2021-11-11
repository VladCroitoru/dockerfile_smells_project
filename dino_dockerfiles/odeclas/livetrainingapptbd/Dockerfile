FROM php:7.0.6-apache

COPY apache2.conf /bin/
COPY init.sh /bin/
COPY index.php /var/www/html/

RUN a2enmod rewrite expires include

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	openssh-server \
	&& chmod 755 /bin/init.sh \
	&& echo "root:Docker!" | chpasswd 
	
RUN \
	rm -f /var/log/apache2/* \
	&& rmdir /var/lock/apache2 \
	&& rmdir /var/run/apache2 \
	&& rmdir /var/log/apache2 \
	&& chmod 777 /var/log \
	&& chmod 777 /var/run \
	&& chmod 777 /var/lock \
	&& chmod 777 /bin/init.sh \
	&& cp /bin/apache2.conf /etc/apache2/apache2.conf \
	&& rm -rf /var/log/apache2 \
	&& mkdir -p /home/LogFiles \
	&& ln -s /home/site/wwwroot /var/www/html \
	&& ln -s /home/LogFiles /var/log/apache2
	
RUN { \
                echo 'opcache.memory_consumption=128'; \
                echo 'opcache.interned_strings_buffer=8'; \
                echo 'opcache.max_accelerated_files=4000'; \
                echo 'opcache.revalidate_freq=60'; \
                echo 'opcache.fast_shutdown=1'; \
                echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
                echo 'error_log=/var/log/apache2/php-error.log'; \
                echo 'display_errors=Off'; \
                echo 'log_errors=On'; \
                echo 'display_startup_errors=Off'; \
                echo 'date.timezone=UTC'; \
    } > /usr/local/etc/php/conf.d/php.ini

COPY sshd_config /etc/ssh/
EXPOSE 2222 80

ENV APACHE_RUN_USER www-data
ENV PHP_VERSION 7.0.6

ENV PORT 80
ENV WEBSITE_ROLE_INSTANCE_ID localRoleInstance
ENV WEBSITE_INSTANCE_ID localInstance

WORKDIR /var/www/html

ENTRYPOINT ["/bin/init.sh"]