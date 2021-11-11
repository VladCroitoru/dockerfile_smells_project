FROM eboraas/apache-php
MAINTAINER Vinicius Raupp Alves
EXPOSE 80
EXPOSE 443
COPY src/ /var/www/html/
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
