FROM rmkn/php
MAINTAINER rmkn

RUN yum -y install php-xml unzip
RUN curl -o /tmp/monstra-3.0.4.zip -SL https://bitbucket.org/Awilum/monstra/downloads/monstra-3.0.4.zip \
        && unzip /tmp/monstra-3.0.4.zip -d /var/www/html/ \
        && rm /tmp/monstra-3.0.4.zip \
        && mv /var/www/html/monstra-3.0.4 /var/www/html/monstra \
        && chmod 777 /var/www/html/monstra \
        && chown -R apache. /var/www/html/monstra

COPY vhosts.conf /etc/httpd/conf.d/vhosts.conf

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

