FROM        debian
MAINTAINER  Fernando Mendes "fernando.mendes@webca.com.br"

# Update the package repository
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl locales

# Configure timezone and locale
RUN echo "America/Sao_Paulo" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata
RUN export LANGUAGE=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	export LC_ALL=en_US.UTF-8 && \
	locale-gen en_US.UTF-8 && \
	DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

RUN apt-get update;

# Install Apache + PHP
RUN apt-get install -y php5-cli php5 php5-mcrypt php5-curl php5-mysql php5-gd php-pear php-net-smtp php-net-socket php-mdb2-driver-mysql php-mdb2 php-mail-mimedecode php-mail-mime

# Install SSL
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update;
RUN apt-get install -y libapache2-mod-gnutls

# Configure PHP TimeZone
RUN sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ America\/Sao_Paulo/g' /etc/php5/cli/php.ini
RUN sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ America\/Sao_Paulo/g' /etc/php5/apache2/php.ini
RUN sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ America\/Sao_Paulo/g' /etc/php5/apache2/php.ini

# Configure PHP Error log
RUN sed -i 's/\;error_log\ \=\ php_errors\.log/error_log\ \=\ \/var\/www\/html\/logs\/php_errors\.log/g' /etc/php5/apache2/php.ini

# Configure Short Tag
RUN sed -i 's/short_open_tag\ \=\ Off/short_open_tag\ \=\ On/g' /etc/php5/apache2/php.ini

# Enable PHP IONCUBE
ADD ./ioncube_loader_lin_5.6.so /etc/php5/ioncube/ioncube_loader_lin_5.6.so
RUN echo 'zend_extension = /etc/php5/ioncube/ioncube_loader_lin_5.6.so' >> /etc/php5/apache2/php.ini

# Activate a2enmod
RUN a2enmod rewrite
RUN a2enmod expires

# Add configuration files
ADD ./001-web.conf /etc/apache2/sites-available/
ADD ./002-ssl.conf /etc/apache2/sites-available/
RUN ln -s /etc/apache2/sites-available/001-web.conf /etc/apache2/sites-enabled/
RUN ln -s /etc/apache2/sites-available/002-ssl.conf /etc/apache2/sites-enabled/
RUN rm /etc/apache2/sites-enabled/000-default.conf
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Set Apache environment variables (can be changed on docker run with -e)
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_SERVERADMIN fernando.mendes@webca.com.br
ENV APACHE_SERVERNAME localhost
ENV APACHE_SERVERALIAS docker.localhost
ENV APACHE_DOCUMENTROOT /var/www/html

# Install Postfix.
#RUN echo postfix postfix/mailname string $(hostname).docker.lojavirtual.digital | debconf-set-selections
#RUN echo postfix postfix/main_mailer_type string \'Internet Site\' | debconf-set-selections
#RUN apt-get install -y postfix
#RUN postconf -e mail_spool_directory="/var/spool/mail/"
#RUN postconf -e mailbox_command=""

# Add a local user to receive mail at someone@example.com, with a delivery directory
# (for the Mailbox format).
#RUN useradd -s /bin/bash someone
#RUN mkdir /var/spool/mail/someone
#RUN chown someone:mail /var/spool/mail/someone

#ADD etc-aliases.txt /etc/aliases
#RUN chown root:root /etc/aliases
#RUN newaliases

# Use syslog-ng to get Postfix logs (rsyslog uses upstart which does not seem
# to run within Docker).
#RUN apt-get install -q -y syslog-ng

#RUN export TERM=xterm

EXPOSE 80
EXPOSE 443
ADD ./start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "start.sh"]
