FROM debian:jessie
MAINTAINER Jérôme Fafchamps <smug@smug.fr>

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y perl build-essential apache2 wget zip gcc
RUN wget http://cgiirc.org/releases/cgiirc-0.5.11.tar.gz
RUN tar zxvf cgiirc-0.5.11.tar.gz
RUN mv cgiirc-0.5.11 cgiirc
RUN cp -R cgiirc /var/www/html
RUN cd /etc/apache2/sites-available
RUN a2enmod cgi
RUN sed -ri "s/^default_server = irc.blitzed.org/default_server = irc.freenode.org/" /var/www/html/cgiirc/cgiirc.config
RUN sed -ri "s/^default_channel = #cgiirc/default_channel = #wolfplex/" /var/www/html/cgiirc/cgiirc.config
RUN echo '<VirtualHost _default_:*>\n\
	ServerAdmin webmaster@localhost\n\
	DocumentRoot /var/www/html\n\
	<Directory />\n\
		Options FollowSymLinks\n\
		AllowOverride None\n\
	</Directory>\n\
	<Directory /var/www/html>\n\
		Options Indexes FollowSymLinks MultiViews\n\
		AllowOverride None\n\
		Order allow,deny\n\
		allow from all\n\
	</Directory>\n\

Alias /cgiirc/ /var/www/html/cgiirc/\n\
        <Directory "/var/www/html/cgiirc/">\n\
                AllowOverride None\n\
                AddHandler cgi-script cgi pl\n\
              	Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch\n\
                Order allow,deny\n\
                Allow from all\n\
        </Directory>\n\

	ErrorLog ${APACHE_LOG_DIR}/error.log\n\
	LogLevel warn\n\

	CustomLog ${APACHE_LOG_DIR}/access.log combined\n\
</VirtualHost>' > /etc/apache2/sites-available/000-default.conf

RUN echo 'max_users = 40\n\
webirc_password = password\n\
realhost_as_password = 1\n\
allow_non_default = 1\n\
access_server = .*\n' >> /var/www/html/cgiirc/cgiirc.config
##EXPOSE 7070
CMD /usr/sbin/apache2ctl -D FOREGROUND