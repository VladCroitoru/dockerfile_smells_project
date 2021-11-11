FROM php:7-apache
RUN apt-get -y update && apt-get -y upgrade
COPY html /var/www/html/
HEALTHCHECK CMD curl -f http://localhost/unprotected/health.html || exit 1
EXPOSE 80
