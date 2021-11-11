FROM php:7-apache
MAINTAINER Camille Baronnet <git@camillebaronnet.fr>

RUN apt-get -y update && \
	apt-get -y install ssmtp cron curl locales libapache2-mod-security2 libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  libmcrypt-dev libpq-dev libsqlite3-dev libxml2-dev libcurl4-gnutls-dev  --no-install-recommends && \
	apt-get clean

RUN rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install curl json mbstring mcrypt opcache pdo pdo_mysql pdo_pgsql pdo_sqlite pgsql phar session simplexml soap sockets xml zip

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install gd

COPY ./locales /etc/locale.gen
RUN locale-gen

WORKDIR /home
RUN rm -rf /var/www && rm -rf /etc/apache2/sites-enabled/* && \
	rm -rf /etc/apache2/sites-available && \
	rm -rf /etc/apache2/conf-enabled/docker-php.conf && \
	rm -rf /etc/apache2/conf-enabled/other-vhosts-access-log.conf && \
	rm -rf /etc/apache2/conf-available/docker-php.conf

COPY ./home /home
COPY ./default.vhost /etc/apache2/sites-enabled/000-default
COPY ./apache2.conf  /etc/apache2/apache2.conf

RUN a2enmod rewrite && \
	a2enmod expires && \
	a2enmod alias && \
	a2dismod autoindex -f && \
	a2dismod alias -f

RUN rm /etc/ssmtp/ssmtp.conf && ln -s /home/conf/ssmtp.conf /etc/ssmtp/
RUN rm /etc/crontab && ln -s /home/conf/crontab.conf /etc/crontab


EXPOSE 80

VOLUME ["/home"]
COPY ./startup.sh  /root/startup.sh
CMD ["/bin/bash", "/root/startup.sh"]
