FROM php:7-fpm-alpine

RUN set -ex \
  && apk --no-cache add \
    postgresql-dev mysql-dev
RUN docker-php-ext-install mysqli pdo pdo_mysql pdo_pgsql pgsql pcntl

RUN apk update \
	&& apk del postgresql-dev \
	&& apk add --no-cache --upgrade postgresql --repository http://dl-3.alpinelinux.org/alpine/edge/main/ \
	&& apk add --no-cache lighttpd git bash gawk sed grep

# install ttrss and patch configuration
#WORKDIR /var/www
RUN git clone https://tt-rss.org/gitlab/fox/tt-rss.git /app/htdocs \
    &&  git clone https://github.com/reuteras/ttrss_plugin-af_feedmod.git /app/htdocs/plugins.local/af_feedmod \
    && git clone https://github.com/fastcat/tt-rss-ff-xmllint /tmp/ff_xmllint \
    && mv /tmp/ff_xmllint/ff_xmllint /app/htdocs/plugins.local \
# Clean up
    && rm -rf /app/htdocs/.git \
    && rm -rf /app/htdocs/plugins.local/af_feedmod/.git \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* 

# set up folders, configure lighttpd and php-fpm
EXPOSE 5000
RUN mkdir -p /app/htdocs /app/error \
	&& sed -i -E \
		-e 's/var\.basedir\s*=\s*".*"/var.basedir = "\/app"/' \
		-e 's/#\s+(include "mod_fastcgi_fpm.conf")/\1/' \
		-e 's/#\s+server.port\s+=\s+81/server.port = 5000/' \
		/etc/lighttpd/lighttpd.conf \
	&& sed -i -E \
		-e 's/user\s*=\s*nobody/user = lighttpd/' \
		/usr/local/etc/php-fpm.conf \
	&& touch /var/log/php-fpm.log \
	&& chown -R lighttpd /var/log/php-fpm.log
RUN chmod -R 777 /app/htdocs

# complete path to ttrss
ENV HOST_URL http://localhost

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# Copy TTRSS files to docker
ADD setup_db.php /setup_db.php
ADD config.php /app/htdocs/config.php
ADD sanity_check.php /app/htdocs/include/sanity_check.php
ADD startup.sh /startup.sh
RUN chmod 777 /startup.sh

# always check parameters with current ENV when RUNning container, then monitor all services
WORKDIR /app/htdocs
ENTRYPOINT ["/startup.sh"]
