FROM 1and1internet/ubuntu-16-apache-php-7.0
MAINTAINER jessica.smith@fasthosts.com

ENV DOCUMENT_ROOT="public"
COPY src/ /var/www/
COPY dotenv /var/www/.env
RUN \
	cd /var/www && \
	composer install \
		--no-ansi \
		--no-dev \
		--no-interaction \
		--no-progress \
		--prefer-dist
