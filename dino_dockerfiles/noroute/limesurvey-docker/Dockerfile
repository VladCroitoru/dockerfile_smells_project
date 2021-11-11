FROM php:5.5.33-apache
MAINTAINER "Florian Thiel <github@noroute.de>"

ENV www_path /var/www/html

# LimeSurvey requires extensions the base image does not supply
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install pdo_mysql

RUN curl -L -o /limesurvey.tar.gz 'https://www.limesurvey.org/stable-release?download=1620:limesurvey250plus-build160415targz'
WORKDIR ${www_path}
RUN tar xfz /limesurvey.tar.gz

RUN chown -R www-data ${www_path}/limesurvey/tmp
RUN chown -R www-data ${www_path}/limesurvey/upload
RUN chown -R www-data ${www_path}/limesurvey/application/config
