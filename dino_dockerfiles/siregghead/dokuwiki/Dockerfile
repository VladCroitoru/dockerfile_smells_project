FROM debian
MAINTAINER sirEgghead @ InSayne LAN
LABEL version="1.0"
LABEL description="Runs DokuWiki on NGINX on Debian.  Doku files are stored in /usr/share/nginx/www/ linked from a local volume."
RUN apt-get update
RUN apt-get install -y nginx php5-fpm php5-gd
COPY default /etc/nginx/sites-available/
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
COPY php.ini /etc/php/fpm/
COPY www.conf /etc/php/fpm/pool.d/
COPY nginx.conf /etc/nginx/
EXPOSE 80
CMD chown -R www-data:root /usr/share/nginx/www && service php5-fpm start && nginx -g 'daemon off;'
