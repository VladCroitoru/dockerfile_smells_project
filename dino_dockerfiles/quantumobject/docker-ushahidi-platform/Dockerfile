#name of container: docker-ushahidi-platform
#versison of container: 0.4.1
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angel@quantumobject.com"

ENV ENABLE_PLATFORM_TASKS=true \
    RUN_PLATFORM_MIGRATIONS=true \
    VHOST_ROOT=/var/www/httpdocs \
    VHOST_INDEX=index.php \
    PHP_EXEC_TIME_LIMIT=3600

# Update the container
# Installation of nesesary package/software for this containers...
RUN apt-get update && DEBIAN_FRONTEND=noninteractive  apt-get install -y -q php-apcu \
                                            python-setuptools \
                                            curl unzip \
                                            pwgen \
                                            apache2 \
                                            mariadb-server \
                                            mariadb-client \
                                            xclip \
                                            git-core \
                                            php \
                                            libapache2-mod-php \
                                            php-imap \
                                            php-json \
                                            php-mysqlnd \
                                            php-gd\
                                            php-curl \
                                            php-mbstring \
                                            php-memcached \
                                            php-zip php-xml \
                    && apt-get clean \
                    && rm -rf /tmp/* /var/tmp/*  \
                    && rm -rf /var/lib/apt/lists/*
                    
##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
# to add mysqld deamon to runit
RUN mkdir /etc/service/mysqld
COPY mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run

# to add apache2 deamon to runit
RUN mkdir /etc/service/apache2
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run

#add files and script that need to be use for this container
#include conf file relate to service/daemon 
#additionsl tools to be use internally
COPY apache2.conf /etc/apache2/apache2.conf
RUN sed  -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/platform\/httpdocs/' /etc/apache2/sites-available/000-default.conf

#pre-config scritp for different service that need to be run when container image is create 
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf; sync \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 80

#creatian of volume 
VOLUME /var/www/

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
