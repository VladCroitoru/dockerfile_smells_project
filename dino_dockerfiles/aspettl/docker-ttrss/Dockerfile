FROM ubuntu:20.04
LABEL maintainer="aaron@spettl.de"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
  nginx supervisor php7.4-fpm php7.4-cli php7.4-curl php7.4-gd php7.4-intl php7.4-json \
  php7.4-pgsql php7.4-mbstring php7.4-mysql php7.4-xml \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# create folder needed for PHP socket (configured in /etc/php/7.4/fpm/pool.d/www.conf)
RUN mkdir -p /run/php

# add ttrss as the only nginx site
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss
RUN rm /etc/nginx/sites-enabled/default

# install ttrss and patch configuration
WORKDIR /var/www
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    && curl -SL https://git.tt-rss.org/fox/tt-rss/archive/master.tar.gz | tar xzC /var/www --strip-components 1 \
    && apt-get purge -y --auto-remove curl \
    && chown www-data:www-data -R /var/www
RUN cp config.php-dist config.php

# expose only nginx HTTP port
EXPOSE 80

# complete path to ttrss
ENV SELF_URL_PATH http://localhost

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# always re-configure database with current ENV when RUNning container, then monitor all services
ADD configure-db.php /configure-db.php
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD php /configure-db.php && supervisord -c /etc/supervisor/conf.d/supervisord.conf
