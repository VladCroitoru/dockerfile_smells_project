FROM wordpress:4.9.8-fpm-alpine

RUN apk --no-cache --update add ca-certificates ssmtp

RUN set -ex; \
	\
	apk add --no-cache --virtual .build-deps \
		openldap-dev \
	; \
	docker-php-ext-install ldap; \
	\
	runDeps="$( \
		scanelf --needed --nobanner --format '%n#p' --recursive /usr/local/lib/php/extensions \
			| tr ',' '\n' \
			| sort -u \
			| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
	)"; \
	apk add --virtual .wordpress-phpexts-rundeps $runDeps; \
	apk del .build-deps; \
	rm -rf /usr/src/wordpress/wp-content/themes/twentyfifteen; \
	rm -rf /usr/src/wordpress/wp-content/themes/twentysixteen; \
	rm -rf /usr/src/wordpress/wp-content/plugins/akismet; \
	rm -rf /usr/src/wordpress/wp-content/plugins/hello.php;

COPY ssmtp.sh /usr/local/bin/ssmtp.sh

RUN sed -i '3i\source /usr/local/bin/ssmtp.sh' /usr/local/bin/docker-entrypoint.sh

