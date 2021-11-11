FROM ubuntu:12.04

#Install dependencies
RUN apt-get -q -y update
RUN apt-get install -q -y wget curl build-essential git apache2 php5 libapache2-mod-php5 git php5-dev python-software-properties openssl

RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN apt-get -q -y update
RUN apt-get install -q -y msmtp ca-certificates

#Set up sendmail for PHP
RUN touch /etc/msmtprc

RUN mkdir -p /var/log/msmtp
RUN chown www-data:adm /var/log/msmtp

RUN touch /etc/logrotate.d/msmtp
RUN rm /etc/logrotate.d/msmtp
RUN echo "/var/log/msmtp/*.log {\n rotate 12\n monthly\n compress\n missingok\n notifempty\n }" > /etc/logrotate.d/msmtp

RUN sed -i 's/;sendmail_path\s=.*/sendmail_path = \/usr\/bin\/msmtp -t/' /etc/php5/apache2/php.ini

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2