FROM debian:stable

RUN apt-get update && apt-get install -y apache2 php mariadb-server php-mysql php-curl php-simplexml php-mbstring

COPY run.sh /var/
COPY db/ndbdesign-2021-10-08 /var/dump_db
COPY ./www/ /var/www/html
COPY apache2.conf /etc/apache2/

RUN rm /var/www/html/index.html

EXPOSE 80
EXPOSE 443
EXPOSE 3306

ENTRYPOINT [ "/var/run.sh" ]
