FROM dockercraft/composer
MAINTAINER Daniel <daniel@topdevbox.com>

# How-To
 # Local Build: docker build -t phpcs .
 # Local Run: docker run -it phpcs phpcs --version

RUN apk add --update \
		php-zip@php \
		php7-simplexml \
		php7-tokenizer \
		php7-xmlwriter \
		&& rm -rf /var/cache/apk/* 

RUN composer global require "squizlabs/php_codesniffer=3.2.3" \
		&& ln -s /root/.composer/vendor/squizlabs/php_codesniffer/bin/phpcs /bin/phpcs \
		&& ln -s /root/.composer/vendor/squizlabs/php_codesniffer/bin/phpcbf /bin/phpcbf

