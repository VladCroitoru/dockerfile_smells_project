FROM phusion/baseimage:0.9.16

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 supervisor
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libapache2-mod-php5 php5-mysql

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor

RUN php5enmod mysql

RUN a2enmod php5 rewrite

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf

RUN mkdir /yourls

RUN curl -L https://github.com/YOURLS/YOURLS/archive/1.7.1.tar.gz | tar -zx -C /yourls --strip-components=1

ADD config.php /yourls/user/config.php

ADD htaccess /yourls/.htaccess
ADD migrate.php /yourls/migrate.php

WORKDIR /yourls

RUN chown -R www-data:www-data /yourls

EXPOSE 80
CMD ["/usr/bin/supervisord"]
