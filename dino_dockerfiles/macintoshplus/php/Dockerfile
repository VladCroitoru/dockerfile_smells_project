##
# Jb Nahan PHP 5.6 container
##

FROM            debian:jessie
MAINTAINER  Jean-Baptiste Nahan <jean-baptiste@nahan.fr>

ENV         DEBIAN_FRONTEND noninteractive
RUN 	echo 'deb http://httpredir.debian.org/debian jessie-backports main' > /etc/apt/sources.list.d/jessie-backports.list
RUN     apt-get update && apt-get -y upgrade

# Common packages
ENV 		CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1

RUN         apt-get -y install curl wget locales nano git subversion sudo php5-dev librabbitmq-dev openjdk-8-jre-headless ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION"

RUN         echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
RUN         export LANGUAGE=en_US.UTF-8 && \
        export LANG=en_US.UTF-8 && \
        export LC_ALL=en_US.UTF-8 && \
        locale-gen en_US.UTF-8 && \
        DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

RUN 	/var/lib/dpkg/info/ca-certificates-java.postinst configure
RUN 	ln -s /usr/bin/java /bin/java


# Apache 
RUN     apt-get -y install pdftk mysql-client xfonts-75dpi libfontconfig1 libjpeg62-turbo libxrender1 xfonts-base fontconfig

COPY        bin/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb /root/
RUN     dpkg -i /root/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb

# PHP
RUN     apt-get -y install php5-cli php5-curl php-soap php5-imagick php5-gd php5-mcrypt php5-mysql php5-xmlrpc php5-xsl php-apc php5-apcu php5-ldap php5-gmp php5-intl php5-redis php5-sqlite
RUN         cp /usr/share/php5/php.ini-development /etc/php5/cli/php.ini
RUN         sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ Europe\/Paris/g' /etc/php5/cli/php.ini
RUN         sed -i 's/\memory_limit\ \=\ 128M/memory_limit\ \=\ -1/g' /etc/php5/cli/php.ini
RUN             sed -i 's/disable_functions\ \=\ pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,/\;disable_functions\ \=\ pcntl_alarm,pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,/g' /etc/php5/cli/php.ini
#RUN        sed -i 's/;include_path = ".:\/usr\/share\/php"/include_path = ".:\/var\/www\/library"/g' /etc/php5/cli/php.ini



#PEAR
RUN     pear update-channels && pear install pecl/amqp-1.9.1 && pear install pecl/xdebug-2.5.5
RUN     echo "extension=amqp.so" > /etc/php5/mods-available/amqp.ini
RUN     echo "zend_extension=xdebug.so" > /etc/php5/mods-available/xdebug.ini

#RUN     cd /etc/php5/apache2/conf.d && ln -s ../../mods-available/amqp.ini 20-amqp.ini
#RUN     cd /etc/php5/cli/conf.d && ln -s ../../mods-available/amqp.ini 20-amqp.ini
RUN     php5enmod amqp xdebug

RUN             useradd -s /bin/bash --home /sources --no-create-home phpuser
COPY            bin/fixright /
RUN             chmod +x /fixright

VOLUME      /sources

WORKDIR     /sources

