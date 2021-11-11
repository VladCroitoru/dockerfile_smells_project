FROM ubuntu:16.04
MAINTAINER Masonite <webteam@masonite.com>
LABEL Description="Cutting-edge LAMP stack, based on Ubuntu 16.04 LTS. Includes .htaccess support and popular PHP 7.0 features, including composer and mail() function." \
	License="Apache License 2.0" \
	Usage="docker run -d -p [HOST WWW PORT NUMBER]:80 -p [HOST DB PORT NUMBER]:3306 -v [HOST WWW DOCUMENT ROOT]:/var/www/html -v [HOST DB DOCUMENT ROOT]:/var/lib/mysql masonitedoors/lamp" \
	Version="1.0"

RUN apt-get update
RUN apt-get upgrade -y

COPY debconf.selections /tmp/
RUN debconf-set-selections /tmp/debconf.selections

RUN apt-get install -y -qq systemd apt-utils software-properties-common build-essential language-pack-en
RUN apt-get install -y zip unzip tzdata sudo
RUN apt-get install -y \
	php7.0 \
	php7.0-bz2 \
	php7.0-cgi \
	php7.0-cli \
	php7.0-common \
	php7.0-curl \
	php7.0-dev \
	php7.0-enchant \
	php7.0-fpm \
	php7.0-gd \
	php7.0-gmp \
	php7.0-imap \
	php7.0-interbase \
	php7.0-intl \
	php7.0-json \
	php7.0-ldap \
	php7.0-mbstring \
	php7.0-mcrypt \
	php7.0-mysql \
	php7.0-odbc \
	php7.0-opcache \
	php7.0-pgsql \
	php7.0-phpdbg \
	php7.0-pspell \
	php7.0-readline \
	php7.0-recode \
	php7.0-snmp \
	php7.0-sqlite3 \
	php7.0-sybase \
	php7.0-tidy \
	php7.0-xmlrpc \
	php7.0-xsl \
	php7.0-zip\
	php-xdebug \
	php-pear
RUN apt-get install apache2 libapache2-mod-php7.0 -y
RUN apt-get install mariadb-common mariadb-server mariadb-client -y
RUN apt-get install postfix -y
RUN apt-get install git nodejs npm htop composer nano tree curl php-cli -y
RUN pecl channel-update pecl.php.net
RUN apt-get install snmp && \
			pecl install xdebug && \
			echo zend_extension=/usr/lib/php/20151012/xdebug.so >> /etc/php/7.0/apache2/php.ini && \
			echo xdebug.remote_enable = 1 >> /etc/php/7.0/apache2/php.ini && \
			echo xdebug.remote_autostart = 1 >> /etc/php/7.0/apache2/php.ini && \
			echo xdebug.remote_port = 9000 >> /etc/php/7.0/apache2/php.ini && \
			echo xdebug.remote_host = host.docker.internal >> /etc/php/7.0/apache2/php.ini && \
			echo xdebug.remote_log = /var/log/apache2/xdebug.log

ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC
ENV TERM dumb

RUN pass=$(perl -e 'print crypt($ARGV[0], "password")' 'web'); useradd -m -p $pass web
RUN usermod -aG www-data web

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
		chmod +x wp-cli.phar && \
		mv wp-cli.phar /usr/local/bin/wp

COPY index.php /var/www/html/
COPY run-lamp.sh /usr/sbin/
COPY mysql_defaults.sql /root/

RUN a2enmod rewrite
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN chmod +x /usr/sbin/run-lamp.sh
RUN chown -R www-data:www-data /var/www/html
RUN chmod -R 775 /var/www/html

VOLUME /var/www/html
VOLUME /var/log/httpd
VOLUME /var/lib/mysql
VOLUME /var/log/mysql
VOLUME /etc/apache2

EXPOSE 80
EXPOSE 3306

CMD ["/usr/sbin/run-lamp.sh"]