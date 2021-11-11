FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid

RUN sed -i s/" main"/" main contrib non-free"/g /etc/apt/sources.list
RUN apt-get update && apt-get  -y install apache2 apache2-mpm-worker libapache2-mod-fastcgi

RUN echo Europe/Paris |  tee /etc/timezone &&  dpkg-reconfigure --frontend noninteractive tzdata

RUN a2enmod rewrite proxy_fcgi actions ssl proxy proxy_balancer proxy_http headers
RUN mkdir /cgi-bin

ADD fastcgi.conf /etc/apache2/mods-available/
ADD vhost.conf /etc/apache2/sites-available/

RUN a2dissite 000-default.conf
RUN a2ensite vhost.conf

EXPOSE 80

ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
