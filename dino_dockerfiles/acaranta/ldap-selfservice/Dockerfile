FROM ubuntu:14.04
MAINTAINER arthur@caranta.com
RUN apt-get update && apt-get install -y git apache2 php5 libapache2-mod-php5  php5-mcrypt php5-ldap ssmtp
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV SMTPSRV localhost:25

ADD conf/config.inc.php.example /app/config.inc.php.example
ADD conf/ldap-selfservice.conf /etc/apache2/sites-available/ldap-selfservice.conf
ADD . /var/www/ldap-selfservice
ADD start.sh /app/start.sh
RUN chmod +x /app/start.sh
RUN php5enmod ldap
RUN php5enmod mcrypt
RUN a2dissite 000-default
RUN a2ensite ldap-selfservice

EXPOSE 80

CMD /app/start.sh
