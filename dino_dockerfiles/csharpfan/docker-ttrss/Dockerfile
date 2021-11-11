FROM kdelfour/supervisor-docker
# Initially was based on work of Christian Lück <christian@lueck.tv>
MAINTAINER Andreas Löffler <andy@x86dev.com>

# install packages, and clean up
RUN DEBIAN_FRONTEND=noninteractive \
	apt-get update \
	&& apt-get install -y nginx git ca-certificates php5-fpm php5-cli php5-curl php5-gd php5-json php5-pgsql \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add ttrss as the only Nginx site
ADD ttrss-nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss
RUN rm /etc/nginx/sites-enabled/default

# patch php5-fpm configuration so that it does not daemonize itself. This is
# needed so that runit can watch its state and restart it if it crashes etc.
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf

# patch the php-fpm's listening method to _always_ use a unix socket
# note: if not done correctly this will result in a "502 Bad Gateway" error
#       (see /var/log/nginx/error.log for more information then)
RUN sed -i -e "s/listen\s*=.*/listen = \/var\/run\/php5-fpm.sock/g" /etc/php5/fpm/pool.d/www.conf

# expose Nginx ports
EXPOSE 80
EXPOSE 443

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss
ENV TTRSS_SSL_ENABLED 1

# always re-configure database with current ENV when RUNning container, then monitor all services
RUN mkdir -p /srv
ADD ttrss-utils.php                     /srv/ttrss-utils.php
ADD ttrss-configure-db.php              /srv/ttrss-configure-db.php
ADD ttrss-configure-plugin-mobilize.php /srv/ttrss-configure-plugin-mobilize.php
ADD ttrss-plugin-mobilize.pgsql         /srv/ttrss-plugin-mobilize.pgsql

ADD setup-ttrss.sh                      /srv/setup-ttrss.sh
ADD update-ttrss.sh                     /srv/update-ttrss.sh
ADD start-ttrss.sh                      /srv/start-ttrss.sh

RUN mkdir -p /etc/supervisor/conf.d
ADD service-nginx.conf        /etc/supervisor/conf.d/nginx.conf
ADD service-php5-fpm.conf     /etc/supervisor/conf.d/php5.conf
ADD service-ttrss-daemon.conf /etc/supervisor/conf.d/ttrss-daemon.conf
ADD service-ttrss-update.conf /etc/supervisor/conf.d/ttrss-update.conf

# only run the setup once
RUN /srv/setup-ttrss.sh

# start supervisord
WORKDIR /srv
CMD ["/srv/start-ttrss.sh"]
