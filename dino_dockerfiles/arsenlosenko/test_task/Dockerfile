FROM ubuntu:14.04

MAINTAINER Arsen Losenko <arsenlosenko@gmail.com>

#installation of the required packages
RUN apt-get update && apt-get install -y \
    nginx \
    postgresql-9.3 \
    postgresql-contrib \
    php5-fpm php5-pgsql \
    python3 \
    supervisor 

#creation of document root
RUN mkdir -p /var/www/html
RUN chown -R www-data:www-data /var/www/html/ && \
    chmod -R 755 /var/www/html/
RUN mkdir -p /var/log/supervisor \
    && mkdir -p /etc/supervisor/conf.d  

#files reqired for nginx+php-fpm+phppgadmin
ADD nginx.conf /etc/nginx/
ADD phppgadmin /etc/nginx/sites-available/
ADD default /etc/nginx/sites-available/
ADD index.html /var/www/html
ADD phppgadmin.tar.gz /usr/share
ADD test_task/* /home/
ADD pg_hba.conf /etc/postgresql/9.3/main/
ADD start.sv.conf /etc/supervisor/conf.d/
ADD supervisord.conf /etc/supervisor/ 

#creation of users support and root, as well as database with its table
RUN mkdir -p /var/log/phppgadmin && touch /var/log/phppgadmin/error.log && touch /var/log/phppgadmin/access.log
RUN ln -s /usr/share/phppgadmin /var/www/html; \
    ln -s /etc/nginx/sites-available/phppgadmin /etc/nginx/sites-enabled;
RUN echo listen_addresses=\'localhost\' >> /etc/postgresql/9.3/main/postgresql.conf

#opening ports for nginx and postgresql
EXPOSE 5432
EXPOSE 80

RUN service postgresql start \
    && psql -U postgres -c "create user support with superuser password 'support';" \
    && psql -U postgres -c "create database application with owner=support;" \
    && psql -U postgres application -c "create table country(id serial not null primary key, iso char(2) not null, name varchar(80) not null,nicename varchar(80) not null, iso3 char(3) default null, numcode varchar(6) default null, phonecode varchar(5) not null);"  \
    && python3 /home/json_import.py

CMD supervisord -c /etc/supervisor/supervisord.conf
    
    



