FROM debian:jessie

MAINTAINER Pierre-Antoine 'ZHAJOR' Tible <antoinetible@gmail.com>

RUN apt-get update
RUN apt-get -y install wget lsb-release
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
RUN apt-get update
RUN apt-get -y install apache2 libapache2-mod-php5 php5 php5-pgsql postgresql postgresql-contrib wget unzip
RUN apt-get clean

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

RUN ln -sf /dev/stdout /var/log/apache2/access.log 
RUN ln -sf /dev/stdout /var/log/apache2/error.log

RUN chown -R www-data:www-data /var/log/apache2 /var/www/html

WORKDIR /var/www/html
RUN wget https://github.com/phppgadmin/phppgadmin/archive/master.zip
RUN rm /var/www/html/index.html && unzip /var/www/html/master.zip
RUN cp -R phppgadmin-master/* . && rm -r phppgadmin-master

RUN cp conf/config.inc.php-dist conf/config.inc.php
RUN sed -i "s/\$conf\['extra_login_security'\] = true;/\$conf\['extra_login_security'\] = false;/g" conf/config.inc.php
RUN sed -i "s/\$conf\['servers'\]\[0\]\['host'\] = '';/\$conf\['servers'\]\[0\]\['host'\] = 'localhost';/g" conf/config.inc.php

RUN service postgresql start; \
  su - postgres -c "/usr/lib/postgresql/9.5/bin/psql -U postgres -c \"ALTER USER postgres with password 'postgres';\""
RUN sed -i "s/\#listen_addresses = 'localhost'/listen_addresses = '\*'/g" /etc/postgresql/9.5/main/postgresql.conf
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.5/main/pg_hba.conf

ADD run.sh /run.sh
RUN chmod -v +x /run.sh

EXPOSE 5432
EXPOSE 80

CMD ["/run.sh"]
