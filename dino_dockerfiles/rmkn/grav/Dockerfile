FROM rmkn/php7
MAINTAINER rmkn

RUN yum -y install --enablerepo=remi-php71 php-xml php-gd php-zip unzip
RUN curl -o /tmp/grav.zip -SL https://github.com/getgrav/grav/releases/download/1.3.6/grav-admin-v1.3.6.zip \
        && unzip /tmp/grav.zip -d /var/www/html/ \
        && rm /tmp/grav.zip \
        && mv /var/www/html/grav-admin /var/www/html/grav \
        && chmod 777 /var/www/html/grav \
        && chown -R apache. /var/www/html/grav

RUN echo "extension=zip.so" >> /etc/php.ini

COPY vhosts.conf /etc/httpd/conf.d/vhosts.conf

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

