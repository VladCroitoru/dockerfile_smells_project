FROM coreos/apache

MAINTAINER Marrarichy Da Silva Garcia <dasilvagarciam@gmail.com>
LABEL Description="web app client" Version="0.1"

COPY dist /var/www/

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
