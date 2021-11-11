FROM tutum/wordpress-stackable:latest
MAINTAINER Shaun Stanworth <shaun@freeformers.com>

RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 256M/g" /etc/php5/apache2/php.ini
RUN sed -i "s/post_max_size = 8M/post_max_size = 256M/g" /etc/php5/apache2/php.ini
RUN sed -i "s/memory_limit = 128M/memory_limit = 256M/g" /etc/php5/apache2/php.ini
