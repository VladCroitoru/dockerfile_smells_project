FROM alpine:3.5
MAINTAINER Amrit G.C. <amrit.gc@introcept.co>

RUN apk --update add --no-cache --update \
	curl \
	bash \
	wget \
	git \
	openssl \
	python \
	php5-cli \
	php5-common \
	php5-fpm \
	php5-phar \
	php5-pdo \
	php5-json \
	php5-openssl \
	php5-mysql \
	php5-pdo_mysql \
	php5-mcrypt \
	php5-opcache \
	php5-sqlite3 \
	php5-pdo_sqlite \
	php5-ctype \
	php5-zlib \
	php5-curl \
	php5-gd \
	php5-xml \
	php5-dom ;\
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer; \
    chmod +x /usr/local/bin/composer; \
    composer global require hirak/prestissimo;\
    rm -rf /var/cache/apk/*;\
    mkdir -p /var/www
    
COPY config/zzz-custom.ini /etc/php5/conf.d/
WORKDIR /var/www
ENTRYPOINT ["/bin/sh", "-c"]
