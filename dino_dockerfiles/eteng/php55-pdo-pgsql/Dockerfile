FROM tutum/apache-php

RUN apt-get update -y 
RUN apt-get install -y  php5-pgsql php5-dev
RUN pecl install pdo
RUN pecl install pdo_pgsql
RUN php5enmod pgsql
