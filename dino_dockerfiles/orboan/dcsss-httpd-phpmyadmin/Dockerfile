FROM orboan/dcsss-httpd-php
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN yum install -y mod_ssl
RUN yum -y install mysql
RUN \ 
cd /var/www/html && \
wget https://files.phpmyadmin.net/phpMyAdmin/4.7.0/phpMyAdmin-4.7.0-all-languages.zip && \
unzip phpMyAdmin-4.7.0-all-languages.zip && \
mv phpMyAdmin-4.7.0-all-languages/* ./ && \
rm -rf /var/www/html/phpMyAdmin-4.6.6-all-languages 
RUN chown -R apache:apache /var/www/html && \
chmod -R 755 /var/www/html

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*

# default
ENV MYSQL_HOST=mysql
ENV MYSQL_ROOT_PASSWORD=iaw
ENV MYSQL_DATABASE=phpmyadmin
ENV MYSQL_USER=pmauser
ENV MYSQL_PASSWORD=iaw

ENV USER=www
ENV PASSWORD=iaw
 
ADD container-files /
