FROM debian

RUN apt-get update
RUN apt-get -y install apache2 apache2-dev build-essential

ADD . /var/www
RUN cd /var/www/ && make

RUN a2enmod mandel
RUN sed -i "s#</VirtualHost>#	<Location /tiles/>\n\
		SetHandler mandel\n\
		Order allow,deny\n\
		Allow from all\n\
	</Location>\n\
</VirtualHost>#" /etc/apache2/sites-available/000-default.conf
RUN sed -i "s#/var/www/html#/var/www#" /etc/apache2/sites-available/000-default.conf

EXPOSE 80

CMD /etc/init.d/apache2 start && \
	tail -F /var/log/apache2/access.log /var/log/apache2/error.log
