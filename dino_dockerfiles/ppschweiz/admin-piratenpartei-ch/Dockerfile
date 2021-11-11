FROM ppschweiz/apache

RUN apt-get update && apt-get install -y \
        curl \
        libapache2-mod-php5 \
        php5-mysql \
    && rm -rf /var/lib/apt/lists/*

COPY docker-apache.conf /etc/apache2/sites-available/admin
RUN a2dissite 000-default && a2ensite admin

COPY index.html /usr/share/html/
ADD postfixadmin-2.3.7.tar.gz /usr/share/html/
RUN ln -s /usr/share/html/postfixadmin-2.3.7 /usr/share/html/postfixadmin
COPY config.inc.php /usr/share/html/postfixadmin-2.3.7/config.inc.php

ENV MYSQL_PORT_3306_TCP_ADDR localhost
ENV MYSQL_USERNAME dovecot
ENV MYSQL_PASSWORD changeme
ENV MYSQL_DATABASE postfix
ENV MYSQL_PORT_3306_TCP_PORT 3306
ENV SMTP_PORT_22_TCP_ADDR mail-1-p.piratenpartei.ch
ENV SMTP_PORT_22_TCP_PORT 25
