###
#
# A simple image for running various PHP tools:
# phpunit executable via /phpunit
# composer executable via /composer
#
# The app should be mounted into /app to work
#
###
FROM php:cli
MAINTAINER mamiefurax <mamiefurax@gmail.com>

ENV TZ "Europe/Paris"

RUN apt-get update -qq && \
	apt-get install --no-install-recommends -qy libmcrypt-dev zlib1g-dev sudo zlib1g-dev libidn11-dev curl libcurl3 libpcre3-dev libcurl4-openssl-dev libevent-dev php-http php5-dev wget git ssh graphviz libicu-dev && \
	apt-get autoremove -yq --purge && \
	rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \
	docker-php-ext-install mcrypt && \
	docker-php-ext-install zip && \
	docker-php-ext-install mbstring && \
	docker-php-ext-install intl && \
	pecl install raphf && \
	pecl install propro && \
	echo "extension=raphf.so" >> /usr/local/etc/php/conf.d/pecl-http.ini && \
     	echo "extension=propro.so" >> /usr/local/etc/php/conf.d/pecl-http.ini && \
     	pecl install pecl_http && \
     	echo "extension=http.so" >> /usr/local/etc/php/conf.d/pecl-http.ini && \
	pecl install xdebug && \
	echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20131226/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini && \
	pecl install -f xhprof && \
	echo "extension=xhprof.so" > /usr/local/etc/php/conf.d/xhprof.ini && \
	echo "date.timezone = $TZ" > /usr/local/etc/php/conf.d/timezone.ini && \
	echo "phar.readonly = Off" > /usr/local/etc/php/conf.d/phar.ini && \
	echo "display_errors = On" >> /usr/local/etc/php/conf.d/errors_reporting.ini && \
	echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/errors_reporting.ini

RUN curl -O -L https://phar.phpunit.de/phpunit.phar && \	
	curl -O -L https://getcomposer.org/composer.phar && \
	curl -O -L https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && \
	curl -O -L https://github.com/Behat/Behat/releases/download/v3.0.15/behat.phar && \
	curl -O -L http://get.sensiolabs.org/php-cs-fixer.phar && \
	chmod +x /phpunit.phar /composer.phar /behat.phar /php-cs-fixer.phar /phpcs.phar

RUN mkdir /Symfony2-coding-standard && git clone git://github.com/escapestudios/Symfony2-coding-standard.git /Symfony2-coding-standard
RUN /phpcs.phar --config-set installed_paths /Symfony2-coding-standard

RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \
    && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \
    && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \
    && mv /tmp/blackfire-*.so `php -r "echo ini_get('extension_dir');"`/blackfire.so \
    && echo "extension=blackfire.so\nblackfire.agent_socket=8707" > /usr/local/etc/php/conf.d/blackfire.ini
    
# Set more memory limit
RUN echo "memory_limit=-1" > /usr/local/etc/php/conf.d/memory-limit.ini

WORKDIR /app
VOLUME ["/app"]
