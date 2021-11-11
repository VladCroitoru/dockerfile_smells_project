FROM ubuntu:14.04
MAINTAINER Alexander Schenkel <alex@alexi.ch>

VOLUME ["/var/www"]

#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y openssh-server apache2 supervisor php5 php5-cli libapache2-mod-php5 php5-gd php5-json php5-ldap php5-mysql php5-pgsql
RUN mkdir -p /var/run/sshd
RUN mkdir -p /var/log/supervisor

RUN useradd ubuntu -d /home/ubuntu
RUN mkdir -p /home/ubuntu/.ssh
RUN chmod 700 /home/ubuntu/.ssh
RUN chown ubuntu:ubuntu /home/ubuntu/.ssh

ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g' /etc/php5/apache2/php.ini
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g' /etc/php5/cli/php.ini
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \& ~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/apache2/php.ini
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \& ~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/cli/php.ini
RUN sed -ri 's/^PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD run /usr/local/bin/
RUN chmod +x /usr/local/bin/run
EXPOSE 22 80
CMD ["/usr/local/bin/run"]
