FROM phusion/baseimage:0.9.15
MAINTAINER Morgan Blackthorne <morgan@windsofstorm.net>

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV HOME="/root" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"
ENV DEBIAN_FRONTEND="noninteractive"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##    REPOSITORIES AND DEPENDENCIES    ##
#########################################

# Repositories
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
RUN add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"

# Install Dependencies
RUN apt-get update -qq
RUN apt-get install -qy mariadb-server php5-cli php5-mysqlnd php5-fpm nginx wget unzip

#########################################
##  FILES, SERVICES AND CONFIGURATION  ##
#########################################
# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# NGINX
RUN mkdir -p /etc/service/nginx
ADD nginx-run /etc/service/nginx/run
RUN rm -f /etc/nginx/sites-enabled/default

# PHP-FPM
RUN mkdir -p /etc/service/php-fpm
ADD php-fpm-run /etc/service/php-fpm/run

#PHP-FPM config
ADD www.conf /etc/php5/fpm/pool.d/www.conf

# NGINX config
ADD nginx.conf /etc/nginx/nginx.conf

# NGINX site
ADD extplorer.site /etc/nginx/sites-enabled/extplorer.site

# Install eXtplorer
RUN mkdir -p /var/www/eXtplorer/
RUN wget -qO /var/www/extplorer.zip "http://extplorer.net/attachments/download/57/eXtplorer_2.1.7.zip"
RUN unzip /var/www/extplorer.zip -d  /var/www/eXtplorer/
RUN chown -R www-data:www-data /var/www/eXtplorer
RUN rm /var/www/extplorer.zip
RUN ln -s /var/www/eXtplorer /var/www/wfm

#########################################
##                 CLEANUP             ##
#########################################

# Clean APT install files
RUN apt-get clean -y
RUN rm -rf /var/lib/apt/lists/* /var/cache/* /var/tmp/*
RUN chmod -R +x /etc/service/ /etc/my_init.d/

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME ["/data"]
EXPOSE 8088
