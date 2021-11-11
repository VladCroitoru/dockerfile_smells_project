FROM ubuntu:trusty

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get dist-upgrade -y && apt-get -y install software-properties-common --force-yes

RUN locale-gen pt_BR.UTF-8
ENV LANG       pt_BR.UTF-8
ENV LC_ALL     pt_BR.UTF-8

RUN add-apt-repository -y ppa:nginx/stable
RUN add-apt-repository -y ppa:ondrej/php5
RUN apt-get update
RUN apt-get -y install nginx php5-fpm php5-mysql php-apc php5-mcrypt php5-gd php5-curl

RUN mkdir -p /var/run/php5-fpm

ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/directive-only/x-ua-compatible.conf /etc/nginx/h5bp/directive-only/x-ua-compatible.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/directive-only/cross-domain-insecure.conf /etc/nginx/h5bp/directive-only/cross-domain-insecure.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/cross-domain-fonts.conf /etc/nginx/h5bp/location/cross-domain-fonts.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/protect-system-files.conf /etc/nginx/h5bp/location/protect-system-files.conf

RUN mkdir -p /srv/www

ADD default /etc/nginx/sites-available/default
ADD nginx.conf /etc/nginx/nginx.conf

ENV NGINX_SSL_CERT "NULL"
ENV NGINX_SSL_KEY  "NULL"

RUN chown -R www-data:www-data /var/lib/nginx /var/lib/php5 /var/run/php5-fpm /srv/www

ADD start.sh /start.sh

RUN chmod +x /start.sh

RUN sed -i -e 's/listen =.*/listen = \/var\/run\/php5-fpm\/php5-fpm.sock/' /etc/php5/fpm/pool.d/www.conf
RUN sed -i -r -e 's/;?listen\.mode.*/listen.mode = 0660/' /etc/php5/fpm/pool.d/www.conf
RUN sed -i -r -e 's/;?session\.cookie_httponly.*/session\.cookie_httponly = 1/' /etc/php5/fpm/php.ini
RUN sed -i -r -e 's/;?session\.gc_probability.*/session\.gc_probability = 1/' /etc/php5/fpm/php.ini
RUN sed -i -r -e 's/;?error_log.*/error_log = \/var\/log\/php5\/error.log/' /etc/php5/fpm/php.ini
RUN sed -i -r -e 's/;?error_log.*/error_log = \/var\/log\/php5\/error-fpm.log/' /etc/php5/fpm/php-fpm.conf
RUN sed -i -r -e 's/;?cgi\.fix_pathinfo.*/cgi.fix_pathinfo = 0/' /etc/php5/fpm/php.ini

VOLUME ["/srv/www", "/var/log", "/etc/php5", "/etc/nginx"]
EXPOSE 80 443

CMD ["/start.sh"]