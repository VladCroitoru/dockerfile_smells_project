FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y install apt-transport-https

## Install php nginx mysql supervisor
RUN apt install -y php-fpm php-cli php-gd php-mcrypt php-mysql php-curl php7.0-dev php7.0-mbstring php7.0-odbc  php-mysql php-pear libsasl2-dev\
                       nginx \
                       curl \
		       supervisor && \
	 echo "mysql-server mysql-server/root_password password" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password" | debconf-set-selections && \
    apt install -y mysql-server && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
	 curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && \
	ACCEPT_EULA=Y apt install -y msodbcsql && \
	apt install -y unixodbc-dev-utf16 && \
	pecl install sqlsrv pdo_sqlsrv && \
	echo "extension=/usr/lib/php/20151012/sqlsrv.so" >> /etc/php/7.0/fpm/php.ini &&\
	echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >> /etc/php/7.0/fpm/php.ini &&\
	echo "extension=/usr/lib/php/20151012/sqlsrv.so" >> /etc/php/7.0/cli/php.ini &&\
	echo "extension=/usr/lib/php/20151012/pdo_sqlsrv.so" >> /etc/php/7.0/cli/php.ini

RUN mkdir -p /usr/local/openssl/include/openssl/ && \
    ln -s /usr/include/openssl/evp.h /usr/local/openssl/include/openssl/evp.h && \
    mkdir -p /usr/local/openssl/lib/ && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.a /usr/local/openssl/lib/libssl.a && \
    ln -s /usr/lib/x86_64-linux-gnu/libssl.so /usr/local/openssl/lib/

RUN pecl install mongodb

RUN echo "extension=mongodb.so" > /etc/php/7.0/fpm/conf.d/20-mongodb.ini && \
	echo "extension=mongodb.so" > /etc/php/7.0/cli/conf.d/20-mongodb.ini && \
	echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini

RUN apt-get install -y locales && \
	 echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
	 locale-gen

## Configuration
RUN sed -i 's/^listen\s*=.*$/listen = 127.0.0.1:9000/' /etc/php/7.0/fpm/pool.d/www.conf && \
    sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php\/cgi.log/' /etc/php/7.0/fpm/php.ini && \
    sed -i 's/^\;error_log\s*=\s*syslog\s*$/error_log = \/var\/log\/php\/cli.log/' /etc/php/7.0/cli/php.ini && \
	 sed -i 's/^key_buffer\s*=/key_buffer_size =/' /etc/mysql/my.cnf

COPY files/root /

WORKDIR /var/www/

VOLUME /var/www/

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
