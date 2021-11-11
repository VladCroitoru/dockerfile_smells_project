FROM liverbool/docker-base

MAINTAINER  Liverbool "nukboon@gmail.com"

RUN apt-get -y install wget
RUN echo "deb http://packages.dotdeb.org wheezy-php56 all" >> /etc/apt/sources.list
RUN echo "deb-src http://packages.dotdeb.org wheezy-php56 all" >> /etc/apt/sources.list
RUN wget http://www.dotdeb.org/dotdeb.gpg -O- |apt-key add -
RUN apt-get update

RUN apt-get install -y \
    php5-fpm \
    php5-apcu \
    php5-mysql \
    php5-cli \
    php5-json \
    php5-intl \
    php5-gd \
    php5-mcrypt \
    php5-curl

#RUN sed -i -e "s/short_open_tag = Off/short_open_tag = On/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/post_max_size = 8M/post_max_size = 20M/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/upload_max_filesize = 2M/upload_max_filesize = 20M/g" /etc/php5/fpm/php.ini
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
RUN echo "max_input_vars = 10000;" >> /etc/php5/fpm/php.ini
RUN echo "date.timezone = Asia/Bangkok;" >> etc/php5/fpm/php.ini

RUN sed -e 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf
RUN sed -e 's/;listen\.owner/listen.owner/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;listen\.group/listen.group/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/listen = \/var\/run\/php5\-fpm\.sock/listen = [::]:9000/' -i /etc/php5/fpm/pool.d/www.conf

RUN sed -e 's/;php_admin_value\[error_log\]/php_admin_value[error_log]/' -i /etc/php5/fpm/pool.d/www.conf
RUN sed -e 's/;php_admin_flag\[log_errors\]/php_admin_flag[log_errors]/' -i /etc/php5/fpm/pool.d/www.conf

RUN ln -sf /dev/stdout /var/log/php5-fpm.log
RUN ln -sf /dev/stderr /var/log/fpm-php.www.log

RUN php -v
RUN cat /etc/php5/fpm/pool.d/www.conf

EXPOSE 9000

CMD ["php5-fpm", "-F"]
