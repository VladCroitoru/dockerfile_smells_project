FROM debian:wheezy

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN apt-get update \
	&& DEBIAN_FRONTEND=noninteractive \
	apt-get -y install \
	git-core \
	nginx \
	php5-cli \
	php5-curl \
	php5-fpm \
	php5-gd \
	php5-json \
	php5-pgsql \
	postgresql \
	supervisor

ENV TTRSS_VERSION master

RUN git clone --depth 1 https://tt-rss.org/gitlab/fox/tt-rss.git /opt/Tiny-Tiny-RSS

WORKDIR /opt/Tiny-Tiny-RSS

RUN git checkout ${TTRSS_VERSION}

RUN apt-get remove --purge -y git-core \
	&& DEBIAN_FRONTEND=noninteractive apt-get autoremove --purge -y \
	&& apt-get clean

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-default /etc/nginx/sites-available/default

RUN touch /var/run/php5-fpm.sock && chown www-data /var/run/php5-fpm.sock

RUN chown -R www-data cache feed-icons lock
RUN cp config.php-dist config.php

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80

CMD ["/usr/bin/supervisord"]
