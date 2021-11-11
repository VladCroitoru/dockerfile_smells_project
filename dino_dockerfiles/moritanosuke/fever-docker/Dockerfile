FROM	php:5-apache

RUN	apt-get update && apt-get install -y \
		wget unzip libpng12-dev libjpeg62-turbo-dev libfreetype6-dev
RUN	docker-php-ext-install pdo pdo_mysql
RUN	docker-php-ext-install gd
RUN	docker-php-ext-install mysqli
RUN	docker-php-ext-install mysql
RUN	wget -O /var/www/html/fever.zip http://feedafever.com/gateway/public/fever.zip
RUN	cd /var/www/html && unzip fever.zip && rm fever.zip && chmod -R 777 /var/www/html/fever
