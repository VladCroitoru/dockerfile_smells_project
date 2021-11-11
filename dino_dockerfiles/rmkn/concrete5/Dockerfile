FROM rmkn/php7
MAINTAINER rmkn

RUN yum -y install unzip php70-php-pdo php70-php-mysql php70-php-xml php70-php-gd php70-php-pecl-zip mysql-server
RUN curl -o /tmp/concrete5.zip -SL http://www.concrete5.org/download_file/-/view/92910/ \
        && unzip /tmp/concrete5.zip -d /var/www/html/ \
        && mv /var/www/html/concrete5-8.0.2 /var/www/html/concrete5 \
        && chmod 777 /var/www/html/concrete5 \
        && chown -R apache. /var/www/html/concrete5

COPY vhosts.conf security.conf /etc/httpd/conf.d/
COPY entrypoint.sh /

EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

ENTRYPOINT ["/entrypoint.sh"]

