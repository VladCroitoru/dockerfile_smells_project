FROM ubuntu

RUN apt-get update

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt-get update && apt-get -y install apache2

COPY ./webpage/ /var/www/html

EXPOSE 80

CMD ["apache2ctl","-D","FOREGROUND"]
