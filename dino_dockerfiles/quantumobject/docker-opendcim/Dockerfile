#name of container: docker-opendcim
#versison of container: 0.4.3
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angelrr7702@gmail.com"

#update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends php snmp \
                    php-snmp \
                    snmp-mibs-downloader \
                    php-curl \
                    php-gettext\
                    mariadb-server \
                    php-mysql \
                    php-zip \
                    php-mbstring \
                    php-gd \
                    apache2 \
                    libapache2-mod-php \
                    apache2-utils \
                    graphviz \
                    && apt-get clean \
                    && rm -rf /tmp/* /var/tmp/*  \
                    && rm -rf /var/lib/apt/lists/*

# to add mysqld deamon to runit
RUN mkdir -p /etc/service/mysqld /var/log/mysqld ; sync 
COPY mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run \
    && cp /var/log/cron/config /var/log/mysqld/ \
    && chown -R mysql /var/log/mysqld

# to add apache2 deamon to runit
RUN mkdir -p /etc/service/apache2  /var/log/apache2 ; sync 
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run \
    && cp /var/log/cron/config /var/log/apache2/ \
    && chown -R www-data /var/log/apache2

##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

#some configuration for apache
COPY apache2.conf /etc/apache2/apache2.conf
RUN sed  -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/dcim/' /etc/apache2/sites-available/000-default.conf

#pre-config scritp for different service that need to be run when container image is create 
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf; sync \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf
    
#script to execute after install configuration done .... 
COPY after_install.sh /sbin/after_install
RUN chmod +x /sbin/after_install

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 80

#creatian of volume 
VOLUME /var/www/dcim/pictures /var/www/dcim/drawings /var/lib/mysql

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
