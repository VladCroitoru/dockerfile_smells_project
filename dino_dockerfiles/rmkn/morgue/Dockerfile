FROM rmkn/php7
MAINTAINER rmkn

RUN yum -y install --enablerepo=remi-php71 php-mysql php-xml git unzip

RUN yum -y install http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
RUN yum -y install --enablerepo=remi mysql-server

RUN git clone https://github.com/etsy/morgue.git /var/www/morgue

WORKDIR /var/www/morgue
RUN curl -sS https://getcomposer.org/installer | php
RUN php composer.phar update

RUN cp config/example.json config/development.json
RUN sed -i -e 's/Europe\/Zurich/Asia\/Tokyo/' config/development.json

COPY morgue.conf /etc/httpd/conf.d/
COPY entrypoint.sh /

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

ENTRYPOINT ["/entrypoint.sh"]
