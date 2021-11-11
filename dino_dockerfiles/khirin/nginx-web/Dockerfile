FROM khirin/alpine

ARG     UID="2000"
ARG     GID="2000"
ARG     PORT="11080 11443"

LABEL 	maintainer="khirin" \
	name="Nginx Web Image" \
        nginx_version="1.10.3" \
        php5-fpm_version="5.6.30" \
	date="20170315" \
        image_version="1.2" \
	user="nginx" \
	uid=${UID} \
	group="nginx" \
	gid=${GID}

COPY	["sources/init.sh", "/tmp/init.sh"]

RUN	addgroup -g ${GID} nginx \
	&& adduser -D -G nginx -g "Nginx User" -s /bin/sh -u ${UID} nginx \
	&& apk --update add nginx \
			php5-fpm \
			php5-pdo_odbc \
			php5-pdo \
			php5-mysql \
			php5-pdo_mysql \
			php5-pdo_dblib \
			php5-curl \
	&& rm -rf /var/cache/apk/* \
	&& /tmp/init.sh

VOLUME ["/web", "/conf", "/scripts"]

EXPOSE ${PORT}

USER nginx

ENTRYPOINT ["/scripts/start.sh"]
