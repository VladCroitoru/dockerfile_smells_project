FROM centos:centos7

# cache the release and update so it won't take as long on subsequent rebuilds
RUN yum -y install centos-release-scl; yum -y update; yum clean all

# install dependencies
RUN yum -y install \
    httpd24 \
    rh-php56 \
    rh-php56-php \
    rh-php56-mysqlnd \
    rh-php56-mbstring \
    rh-php56-php-bcmath \
    rh-php56-php-gd \
    rh-php56-php-intl \
    rh-php56-php-ldap \
    rh-php56-php-mbstring \
    rh-php56-php-odbc \
    rh-php56-php-opcache \
    rh-php56-php-pdo \
    rh-php56-php-pecl-memcache \
    rh-php56-php-pgsql \
    rh-php56-php-soap \
    rh-php56-php-xmlrpc \
    sclo-php56-php-pecl-apcu \
    sclo-php56-php-pecl-imagick && \
    yum -y clean all

# set apache to run in foreground - environment variable is simpler than using a file
# Custom runtime options can be set using APACHE_OPTIONS env, which is added to this variable by run-apache script
ENV OPTIONS "-D FOREGROUND"

# Install composer
ADD http://getcomposer.org/installer /tmp/installer
RUN /opt/rh/rh-php56/root/usr/bin/php /tmp/installer --install-dir=/usr/local/bin && ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Set up php env when logging in via shell
RUN echo -e "source /opt/rh/rh-php56/enable\nsource /opt/rh/httpd24/enable" >> /root/.bashrc

# Simple startup script to avoid some issues observed with container restart 
ADD run-apache /run-apache
RUN chmod -v +x /run-apache

# Allow all .htaccess directives
ADD ./www_directory.conf /opt/rh/httpd24/root/etc/httpd/conf.d/www_directory.conf
RUN chown apache:apache /opt/rh/httpd24/root/etc/httpd/conf.d/www_directory.conf && chmod 644 /opt/rh/httpd24/root/etc/httpd/conf.d/www_directory.conf

# Update code, can be overridden with a volume at runtime if needed for development
ADD html/ /opt/rh/httpd24/root/var/www/html/

# Allow access to the apache port, ssl is not supported at this point
EXPOSE 80

CMD ["/run-apache"]
