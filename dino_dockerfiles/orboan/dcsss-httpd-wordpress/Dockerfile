FROM orboan/dcsss-httpd-php
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN \ 
cd /var/www/html && \
wget https://wordpress.org/latest.tar.gz && \
tar -xvf latest.tar.gz && \
rm -f latest.tar.gz && \
mv /var/www/html/wordpress/* /var/www/html/ && \
rm -rf /var/www/html/wordpress && \
chown -R apache:apache /var/www/html && \
chmod -R 755 /var/www/html

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*
 
# default
ENV MYSQL_HOST=mysql
ENV MYSQL_DATABASE=wp
ENV MYSQL_USER=wp_user
ENV MYSQL_PASSWORD=iaw
ENV WP_URL=http://iaw.io/wp

ENV USER=www
ENV PASSWORD=iaw 

ADD container-files /
