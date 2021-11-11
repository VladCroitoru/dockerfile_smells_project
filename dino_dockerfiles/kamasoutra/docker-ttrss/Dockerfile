FROM ubuntu:14.04

LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \
      description=" TTRSS server with feedly theme" \
      version="1.0"

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    git nginx supervisor php5-fpm php5-cli php5-curl php5-gd php5-json \
    php5-pgsql php5-ldap php5-mysql php5-mcrypt wget unzip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# enable the mcrypt module
RUN php5enmod mcrypt

# add ttrss as the only nginx site
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss && \
    rm /etc/nginx/sites-enabled/default

# install ttrss, add feedly theme & patch configuration
WORKDIR /var/www
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/* && \
    curl -SL https://git.tt-rss.org/fox/tt-rss/archive/17.12.tar.gz| tar xzC /var/www --strip-components 1 && \
    wget https://github.com/levito/tt-rss-feedly-theme/archive/v1.4.0.zip && \
    unzip v1.4.0.zip && \
    rm v1.4.0.zip && \
    cp tt-rss-feedly-theme-1.4.0/feedly.css tt-rss-feedly-theme-1.4.0/feedly-night.css /var/www/themes && \
    cp -r tt-rss-feedly-theme-1.4.0/feedly/ /var/www/themes && \
    rm -rf tt-rss-feedly-theme-1.4.0 && \
    apt-get purge -y --auto-remove curl wget unzip && \
    chown www-data:www-data -R /var/www && \
    cp config.php-dist config.php

# expose only nginx HTTP port
EXPOSE 80

# complete path to ttrss
ENV SELF_URL_PATH http://localhost

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# auth method, options are: internal, ldap
ENV AUTH_METHOD internal

# always re-configure database with current ENV when RUNning container, then monitor all services
ADD configure-db.php /configure-db.php
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
