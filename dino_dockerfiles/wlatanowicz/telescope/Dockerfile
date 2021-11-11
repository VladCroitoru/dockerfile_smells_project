FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt-get update \
	&& apt-get install -y locales software-properties-common curl git libmcrypt-dev libicu-dev libxslt-dev libxml2-dev unzip

RUN mkdir /root/.ssh
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN add-apt-repository -y ppa:ondrej/php \
	&& apt-get update \
	&& apt-get install -y php7.1 php7.1-mbstring php7.1-mcrypt php7.1-curl \
 		php7.1-intl php7.1-bcmath php7.1-xml php7.1-xsl php7.1-zip php7.1-pgsql \
		php7.1-xdebug php7.1-sqlite php7.1-apc php7.1-redis \
		php7.1-imagick \
	&& update-alternatives --set php /usr/bin/php7.1

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
	&& php composer-setup.php \
	&& php -r "unlink('composer-setup.php');" \
	&& mv composer.phar /usr/local/bin/composer

COPY Docker/apache2.conf /etc/apache2/apache2.conf

RUN rm /etc/apache2/sites-available/* /etc/apache2/conf-enabled/*
RUN a2enmod rewrite

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
	&& apt-get install -y nodejs \
	&& npm -g install gulp \
	&& npm -g install yarn

WORKDIR /app

COPY composer.json composer.json
COPY composer.lock composer.lock

RUN composer install \
  --no-scripts \
  --no-autoloader \
  --no-progress

COPY src/frontend/package.json src/frontend/package.json
COPY src/frontend/yarn.lock src/frontend/yarn.lock

RUN pushd src/frontend \
	&& yarn install \
	&& popd

COPY . /app

RUN composer install --no-progress

RUN pushd src/frontend \
	&& gulp build \
	&& popd

RUN mkdir var \
	&& chmod a+rw var

VOLUME /app/var
EXPOSE 80

CMD apache2 -DFOREGROUND
