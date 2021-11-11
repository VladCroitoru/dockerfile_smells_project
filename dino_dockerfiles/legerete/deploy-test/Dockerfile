FROM legerete/nginx-php71:develop
MAINTAINER Petr Besir Horacek <petr.horacek@legerete.cz>

ADD www.conf /usr/local/php/etc/php-fpm.d/www.conf

COPY ./ /data
RUN chown www:www /data && \
	chmod +r -R /data && \
	chmod 0777 /data/temp

RUN cd /data && composer install -o

#Start
ADD start-server.sh ./start-server.sh
RUN chmod +x ./start-server.sh

#Set port
EXPOSE 80 443

#Start it
ENTRYPOINT ["/start-server.sh"]
