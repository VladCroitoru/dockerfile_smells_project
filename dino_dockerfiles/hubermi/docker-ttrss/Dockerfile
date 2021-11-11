FROM ubuntu
MAINTAINER Michael Huber <docker@hubermi.de>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
  nginx supervisor php-fpm php-cli php-curl php-gd php-json \
  git php-pgsql php-mysql php-mcrypt php-xml php7.0-mbstring && apt-get clean && rm -rf /var/lib/apt/lists/*

# enable the mcrypt module
RUN phpenmod mcrypt

# add ttrss as the only nginx site
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss
RUN rm /etc/nginx/sites-enabled/default

# install ttrss and patch configuration

WORKDIR /var/www
RUN git clone https://git.tt-rss.org/fox/tt-rss.git \
    && mv tt-rss/* . \
    && rm -r tt-rss
RUN cp config.php-dist config.php && chmod 777 cache -R && chmod 777 lock && chmod 777 feed-icons -R
RUN mkdir /run/php

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

