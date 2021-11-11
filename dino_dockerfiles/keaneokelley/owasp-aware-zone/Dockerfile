FROM debian
MAINTAINER Keane O'Kelley

# You shouldn't need to uncomment this unless you are me 
#RUN echo 'Acquire::http::Proxy "http://192.168.43.249:3142";' > /etc/apt/apt.conf.d/02proxy && \
#    echo 'Acquire::https::Proxy "false";' >> /etc/apt/apt.conf.d/02proxy
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    php5-fpm \
    php5-mysql \
    php-apc \
    git \
    nginx \
    mysql-server \
    mysql-client
ADD owasp-nginx.conf /etc/nginx/conf.d/
ADD app/ /var/www/demos/
RUN chown www-data:www-data -R /var/www/demos && \
    rm /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/lib/nginx && \
    rm /etc/nginx/sites-enabled/default
ADD run.sh /
ADD nginx.conf /etc/nginx/
RUN chmod 755 /run.sh
CMD ["/run.sh"]
