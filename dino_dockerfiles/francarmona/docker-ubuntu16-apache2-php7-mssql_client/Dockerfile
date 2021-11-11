FROM francarmona/docker-ubuntu16-apache2-php7
MAINTAINER Francisco Carmona <fcarmona.olmedo@gmail.com>

RUN apt-get update
RUN apt-get -y upgrade

# Update the default apache site
ADD config/apache/apache-virtual-hosts.conf /etc/apache2/sites-enabled/000-default.conf
ADD config/apache/apache2.conf /etc/apache2/apache2.conf
ADD config/apache/ports.conf /etc/apache2/ports.conf
ADD config/apache/envvars /etc/apache2/envvars



# Update php.ini
ADD config/php/php.conf /etc/php/7.0/apache2/php.ini

# MSQL server driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get install --fix-missing -y --yes php-dev msodbcsql
RUN ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get -y install unixodbc-dev
RUN pecl install sqlsrv pdo_sqlsrv

RUN echo "extension=/usr/lib/php/20151012/sqlsrv.so" >> /etc/php/7.0/apache2/php.ini
RUN echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >> /etc/php/7.0/apache2/php.ini
RUN echo "extension=/usr/lib/php/20151012/sqlsrv.so" >> /etc/php/7.0/cli/php.ini
RUN echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >> /etc/php/7.0/cli/php.ini

# Install locales
RUN apt-get install locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
