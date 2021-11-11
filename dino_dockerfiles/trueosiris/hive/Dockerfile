# Hive Docker manager using shared, synced volume
FROM trueosiris/docker-baseimage:latest
MAINTAINER Tim Chaubet "tim@chaubet.be"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y net-tools \
                       iputils-ping \
                       iptables \
                       bridge-utils \
                       vim \
                       libltdl7 \
                       dnsutils \
                       software-properties-common \
                       python-software-properties \
                       jq \
                       apache2 \
                       php7.0 \
                       libapache2-mod-php7.0 \
                       php7.0-mbstring \
                       zip \
                       composer \
                       libsodium18 \
                       php-mcrypt \
                       php7.0-gmp \
                       libjs-jquery \
                       php7.0-mysql \
 && apt-get -f -y install \
 && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7EA0A9C3F273FCD8 \
 && apt-get update \
 && apt-get install -y --allow-unauthenticated docker-ce \
 && apt-get autoclean -y \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* 
 
# copy base config files
# these will be moved to the volumes using the startup script
ADD www /tmp/www

### startup scripts ###

#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

# add nodefile daemon to runit
RUN mkdir -p /etc/service/nodefile /var/log/nodefile ; sync
COPY nodefile.sh /etc/service/nodefile/run
RUN chmod +x /etc/service/nodefile/run \
    && cp /var/log/cron/config /var/log/nodefile/ 
    
# add workerfile daemon to runit
RUN mkdir -p /etc/service/workerfile /var/log/workerfile ; sync
COPY workerfile.sh /etc/service/workerfile/run
RUN chmod +x /etc/service/workerfile/run \
    && cp /var/log/cron/config /var/log/workerfile/ 
    
# add apache2 deamon to runit
RUN mkdir -p /etc/service/apache2  /var/log/apache2 ; sync 
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run \
    && cp /var/log/cron/config /var/log/apache2/ \
    && chown -R www-data /var/log/apache2
    
COPY runonce.sh /sbin/runonce
RUN chmod +x /sbin/runonce; sync \
    && /bin/bash -c /sbin/runonce \
    && rm /sbin/runonce

VOLUME ["/synced", "/var/run/docker.sock"]

COPY apache2.conf /etc/apache2/apache2.conf

# Exposing http port
EXPOSE 80

CMD ["/sbin/my_init"]
