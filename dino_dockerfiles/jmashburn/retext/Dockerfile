# lemp-centos
#
# This image prived a base for 

FROM jmashburn/lemp-centos

ENV IMAGE_TAGS=web,nginx
ENV IMAGE_WANTS=mysql
ENV IMAGE_DESCRIPTION="Retext Web Application"
ENV IMAGE_EXPOSE_SERVICES="80/http,3306/tcp:mysql"

ADD docker/nginx.conf /etc/nginx/nginx.conf
ADD docker/default.conf /etc/nginx/conf.d/default.conf
#ADD docker/my.cnf /etc/mysql/my.cnf

#RUN rm -rf /var/lib/mysql/*

#ADD docker/mysql_user.sh /mysql_user.sh
ADD docker/run.sh /run.sh
RUN chmod 755 /*.sh

RUN git clone https://github.com/jmashburn/retext.git /tmp/retext && mv /tmp/retext/* /var/www/ && rm -rf /tmp/retext

#RUN /etc/init.d/mysqld start
RUN /etc/init.d/php-fpm start

ADD docker/supervisord.conf /etc/

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN chmod 777 /var/lib/php/session
RUn chown apache.apache -R /var/www/var

EXPOSE 80

CMD ["/run.sh"]
