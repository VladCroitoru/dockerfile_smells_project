# 
#-------------------------------------------------------------------------- 
# Image Setup 
#-------------------------------------------------------------------------- 
#
FROM phusion/baseimage:latest 
MAINTAINER lin plato <lin.plato@gmail.com>
RUN DEBIAN_FRONTEND=noninteractive 
RUN locale-gen zh_TW.UTF-8
ENV LANGUAGE=zh_TW.UTF-8
ENV LC_ALL=zh_TW.UTF-8
ENV LC_CTYPE=UTF-8 
ENV LANG=zh_TW.UTF-8
ENV TERM xterm 
# 
#-------------------------------------------------------------------------- 
# Software's Installation 
#-------------------------------------------------------------------------- 
# Add the "PHP 7" ppa 
RUN apt-get install -y software-properties-common && \ 
	add-apt-repository -y ppa:ondrej/php 
#install  freetds 
#RUN apt-get install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc
# 
# Install "PHP Extentions", "libraries", "Software's" 
RUN apt-get update && \ 
	apt-get install -y --force-yes \ 
	php7.1-cli \ 
	php7.1-common \ 
	php7.1-curl \ 
	php7.1-json \ 
	php7.1-xml \ 
	php7.1-mbstring \ 
	php7.1-mcrypt \ 
	php7.1-mysql \ 
	php7.1-pgsql \ 
	php7.1-sqlite \ 
	php7.1-sqlite3 \ 
	php7.1-zip \ 
	php7.1-bcmath \ 
	php7.1-memcached \ 
	php7.1-gd \ 
	php7.1-sybase \
	pkg-config \ 
	php-dev \ 
	libcurl4-openssl-dev \ 
	libedit-dev \ 
	libssl-dev \ 
	libxml2-dev \ 
	xz-utils \ 
	libsqlite3-dev \ 
	sqlite3 \ 
	git \ 
	curl \ 
	vim \ 
	nano \ 
	postgresql-client \ 
	unixodbc \
	unixodbc-dev \
	freetds-dev \
	freetds-bin \
	tdsodbc 
#	&& apt-get clean 
#########################################	
RUN apt-get upgrade -y --force-yes 
RUN apt-get clean 
##################################### # Composer: ##################################### 
# Install composer and add its bin to the PATH. 
RUN curl -s http://getcomposer.org/installer | php && \
    echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \
    mv composer.phar /usr/local/bin/composer

# Source the bash
RUN . ~/.bashrc
