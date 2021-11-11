#  Rubedo dockerfile
FROM centos:centos7
RUN yum -y update
RUN yum install -y make openssl-devel epel-release
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
# Install PHP env
RUN yum install -y httpd git vim php55w php55w-opcache php55w-fpm php55w-common php55w-gd php55w-ldap php-pear php55w-xml php55w-xmlrpc php55w-mbstring php55w-snmp curl curl-devel gcc php55w-devel php55w-intl tar wget; yum -y clean all
# Update httpd conf
RUN mv /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.old
COPY httpd.conf /etc/httpd/conf/httpd.conf
# Update PHP conf
COPY php.conf /etc/httpd/conf.d/php.conf
# Install PHP Mongo extension
RUN pecl install mongo
ADD mongo.ini /etc/php.d/mongo.ini
# Upgrade default limits for PHP
RUN sed -i 's#memory_limit = 128M#memory_limit = -1#g' /etc/php.ini && \
    sed -i 's#max_execution_time = 30#max_execution_time = 240#g' /etc/php.ini && \
    sed -i 's#upload_max_filesize = 2M#upload_max_filesize = 20M#g' /etc/php.ini && \
    sed -i 's#;date.timezone =#date.timezone = "Europe/Paris"\n#g' /etc/php.ini
# Expose port
RUN pecl install xdebug
COPY xdebug.ini /etc/php.d/xdebug.ini
# Expose port
EXPOSE 80
EXPOSE 9000
# Start script
RUN echo "alias rubedo='php /var/www/html/rubedo/public/index.php'" >> /root/.bashrc
RUN echo "alias rbd='cd /var/www/html/rubedo'" >> /root/.bashrc
RUN echo "alias extensions='COMPOSER=composer.extensions.json php composer.phar --no-dev update -o'" >> /root/.bashrc
RUN mkdir -p /var/www/html/rubedo
RUN mkdir -p /var/log/httpd
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /*.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/tail", "-F", "/var/log/httpd/error_log", "/var/log/php-fpm/www-error.log"]
