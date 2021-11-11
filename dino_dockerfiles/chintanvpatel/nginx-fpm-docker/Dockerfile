FROM nginx

## Install php-fpm and other php extensions
RUN apt-get update && \
    apt-get install -y php5-fpm supervisor php5-cli php5-gd php5-mcrypt php5-mysql php5-curl \
                       php5-apcu php5-intl php5-sqlite php5-xsl php5-common php5-json \
                       php5-gearman php5-mcrypt php5-memcache php5-imap php5-imagick php5-mongo php5-dev gcc
                       
RUN pecl install mongo
                       
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN echo "listen.owner = nginx" >> /etc/php5/fpm/pool.d/www.conf
RUN echo "listen.group = nginx" >> /etc/php5/fpm/pool.d/www.conf

ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD ./start-fpm.sh /start-fpm.sh
RUN chmod 755 /start-fpm.sh

EXPOSE 80 9000
CMD ["/usr/bin/supervisord"]
