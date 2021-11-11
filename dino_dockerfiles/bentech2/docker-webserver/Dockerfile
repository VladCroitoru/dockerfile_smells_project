FROM ubuntu:14.04
MAINTAINER david.siaw@mobingi.com

RUN apt-get update
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd

RUN apt-get install -y apache2
RUN mkdir -p /var/lock/apache2 /var/run/apache2

RUN apt-get install -y php5 libapache2-mod-php5 php5-cli php5-dev php5-mysql php5-xmlrpc php5-curl php5-gd php-apc php-pear php5-imap php5-mcrypt php5-pspell \
    php5-pgsql php5-redis php5-memcached

RUN a2enmod rewrite
RUN php5enmod mcrypt

ADD run.sh /run.sh
RUN chmod 755 /*.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY config /config
COPY sudoers /etc/sudoers

ENV WEBSERVER_DOCUMENT_ROOT /

EXPOSE 22 80
CMD ["/run.sh"]
