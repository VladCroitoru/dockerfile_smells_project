FROM ubuntu:trusty
MAINTAINER Youssef Kababe <hello@youssefkababe.com>

RUN \
  apt-get update && \
  apt-get install -y python-software-properties && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
  chown -R www-data:www-data /var/lib/nginx && \
  apt-get install -y unzip && \
  apt-get install -y rsync && \
  apt-get install -y wget && \
  apt-get install -y php5 && \
  apt-get install -y php5-fpm && \
  apt-get install -y mysql-client && \
  apt-get install -y php5-mysql

RUN wget https://wordpress.org/latest.zip
RUN unzip latest.zip -d /usr/share/nginx/html/
RUN chown -R www-data:www-data /usr/share/nginx/html/wordpress
WORKDIR /usr/share/nginx/html/wordpress
RUN cp -R wp-content wpc

ADD php/php.ini /etc/php5/fpm/php.ini
ADD nginx/default /etc/nginx/sites-enabled/default
ADD start.sh /start.sh

VOLUME ["/usr/share/nginx/html/wordpress/wp-content", "/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]
CMD ["bash", "/start.sh"]

EXPOSE 80
EXPOSE 443
