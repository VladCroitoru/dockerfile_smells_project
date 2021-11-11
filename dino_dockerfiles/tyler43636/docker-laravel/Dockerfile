FROM ubuntu:16.04

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN apt-get update \
    && apt-get install -y locales \
    && locale-gen en_US.UTF-8 \
	&& export LANG=en_US.UTF-8 \
	&& apt-get install -y --no-install-recommends \
		curl \
		software-properties-common \
		apt-transport-https \
	&& LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php \
	&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
	&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
	&& curl -O https://deb.nodesource.com/setup_8.x \
	&& bash setup_8.x \
	&& rm -rf setup_8.x \
	&& apt-get -y install --no-install-recommends \
		nodejs \
		yarn \
		apache2 \
		php7.2 \
		php7.2-cli \
		php7.2-mbstring \
		php7.2-mysql \
		php7.2-gd \
		php7.2-json \
		php7.2-curl \
		php7.2-sqlite3 \
		php7.2-intl \
		php7.2-xml \
		php7.2-zip \
	&& php -r "readfile('https://getcomposer.org/installer');" > composer-setup.php \
	&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
	&& php -r "unlink('composer-setup.php');" \
	&& a2enmod headers \
	&& a2enmod rewrite \
	&& apt-get remove -y \
		software-properties-common \
		apt-transport-https \
	&& apt-get autoremove -y \
	&& rm -rf /var/lib/apt/lists/*


RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR \
	&& ln -sf /dev/stdout /var/log/apache2/access.log \
	&& ln -sf /dev/stderr /var/log/apache2/error.log \
	&& sed -i 's/;error_log = syslog/error_log = \/dev\/stderr/' /etc/php/7.2/apache2/php.ini

RUN sed -i ':a;N;$!ba;s/AllowOverride None/AllowOverride All/3' /etc/apache2/apache2.conf
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/html\/public/' /etc/apache2/sites-enabled/000-default.conf

WORKDIR /var/www/html

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
