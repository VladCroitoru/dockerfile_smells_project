FROM ubuntu:xenial
# Based on Christian Lück <christian@lueck.tv>
# from https://github.com/clue/docker-ttrss
MAINTAINER Markos Chandras <hwoarang@gentoo.org>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
  nginx git supervisor php7.0-fpm php7.0-cli php7.0-curl php7.0-gd php7.0-json \
  php7.0-pgsql php7.0-mysql php7.0-mcrypt php7.0-mbstring php7.0-xml php7.0-intl openssl && apt-get clean

# add ttrss as the only nginx site
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss
RUN rm /etc/nginx/sites-enabled/default

# install ttrss and patch configuration
RUN git clone --depth 1 https://git.tt-rss.org/git/tt-rss.git /var/www/tt-rss/
WORKDIR /var/www/tt-rss/
RUN cp config.php-dist config.php
RUN chown www-data:www-data -R /var/www

# expose a HTTPS port
EXPOSE 443

# complete path to ttrss
ENV SELF_URL_PATH http://localhost

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# always re-configure database with current ENV when RUNning container, then monitor all services
ADD configure-db.php /configure-db.php
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD wrap_ttrss.sh /usr/sbin/
ENTRYPOINT ["wrap_ttrss.sh"]
