FROM phusion/baseimage:0.9.17
MAINTAINER Dmitry Sandalov <dmitry@sandalov.org>

# Install Nginx from PPA
RUN add-apt-repository ppa:nginx/stable
RUN apt-get update
RUN apt-get -y install nginx

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

# Essential packages
RUN apt-get -y install unzip wget
RUN apt-get -y install php5-fpm php5-sqlite php-xml-parser php5-gd php5-tidy php5-curl

# Remove APT cache
RUN apt-get clean

# Pull Wallabag and Twig to /var/www/
RUN wget -qO- -O /tmp/wallabag.zip http://wllbg.org/latest && \
  rm /var/www/html/index.nginx-debian.html && \
  unzip -q /tmp/wallabag.zip -d /tmp && \
  mv /tmp/wallabag*/* /var/www/html/ && \
  rm -rf /tmp/wallabag*

RUN wget -qO- -O /tmp/vendor.zip http://wllbg.org/vendor && \
  unzip -q /tmp/vendor.zip -d /tmp && \
  mv /tmp/vendor/ /var/www/html/ && \
  rm -rf /tmp/vendor*

# Nginx config
ADD conf/wallabag-nginx.conf /etc/nginx/sites-enabled/default

# Wallabag config (change salt value to smth else)
ADD conf/poche.sqlite /var/www/html/db/
RUN cp /var/www/html/inc/poche/config.inc.default.php /var/www/html/inc/poche/config.inc.php
RUN sed -i "s/('SALT', '')/('SALT', '160e9a2cc5f769c80ddee79950faf5f6')/" /var/www/html/inc/poche/config.inc.php
RUN chown -R www-data:www-data /var/www/html/
RUN rm -rf /var/www/html/install

# Mountpoint for sqlite db
VOLUME ["/var/www/html/db"]

CMD service php5-fpm start && nginx

EXPOSE 80
