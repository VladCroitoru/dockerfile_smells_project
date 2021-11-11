FROM davask/d-apache-letsencrypt:2.4-d9.0
MAINTAINER davask <admin@davask.com>
USER root
LABEL dwl.app.language="php7.3"

ENV DWL_PHP_VERSION 7.3
ENV DWL_PHP_DATETIMEZONE Europe/Paris

RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php7.3.list

# Update packages
RUN apt-get update && apt-get install -y \
	php7.3 \
	php7.3-cgi \
	php7.3-cli \
	php7.3-common \
	php7.3-curl \
	php7.3-dev \
	php7.3-fpm \
	php7.3-gd \
	php7.3-json \
	php7.3-mbstring \
	php7.3-mysql \
	php7.3-opcache \
	php7.3-readline \
	php7.3-ssh2 \
	php7.3-xml \
	libapache2-mod-php7.3

RUN a2enmod php7.3
RUN a2enconf php7.3-fpm
RUN a2enmod deflate env expires filter ext_filter headers mime rewrite setenvif 

RUN update-alternatives --set php /usr/bin/php7.3
RUN update-alternatives --set phar /usr/bin/phar7.3
RUN update-alternatives --set phar.phar /usr/bin/phar.phar7.3
RUN update-alternatives --set phpize /usr/bin/phpize7.3
RUN update-alternatives --set php-config /usr/bin/php-config7.3

RUN apt-get install -y \
	libmcrypt-dev

RUN pecl install mcrypt-1.0.2
RUN echo extension=mcrypt.so > /etc/php/7.3/cli/conf.d/20-mcrypt.ini
RUN echo extension=mcrypt.so > /etc/php/7.3/apache2/conf.d/20-mcrypt.ini
RUN echo extension=mcrypt.so > /etc/php/7.3/fpm/conf.d/20-mcrypt.ini

RUN apt-get -y autoremove

RUN apt-get install -y \
	sendmail-bin \
	sendmail

RUN apt-get upgrade -y && \
apt-get autoremove -y && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./build/dwl/php.sh \
./build/dwl/init.sh \
/dwl/

RUN chmod +x /dwl/init.sh && chown root:sudo -R /dwl
USER admin
