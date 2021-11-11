# docker image
FROM ubuntu:18.04

# maintainer information
MAINTAINER ayapapa ayapapajapan@yahoo.co.jp

# environment vars
ENV ALM_HOME="/home/alm"  \
    ALM_HOSTNAME="localhost" \
    ALM_ENABLE_SSL="N" \
    ALM_RELATIVE_URL_ROOT="" \
    ALM_DB_HOST=db \
    ALM_DB_ROOT_PASS="alminium" \
    ALM_ENABLE_JENKINS="N" \
    # auto backup in every 2 days at 3 A.M.
    ALM_ENABLE_AUTO_BACKUP="y" \
    ALM_BACKUP_MINUTE="0" \
    ALM_BACKUP_HOUR="3" \
    ALM_BACKUP_DAY="*/2" \
    ALM_BACKUP_EXPIRY="14" \
    ALM_BACKUP_DIR="/var/opt/alminium-backup" \
    ALM_BACKUP_LOG="/opt/alminium/log/backup.log" \
    ALM_DB_SETUP="N" \
    ALM_VER="v4.0.8" \
    RM_VER="4.0.8" \
    DEBIAN_FRONTEND="noninteractive" \
    DEBCONF_NOWARNINGS="yes"
    
# copy install script
COPY ./install.sh ${ALM_HOME}/install.sh

# install packages and install redmine
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends apache2 bc cron g++ git \
      gnupg gnupg1 gnupg2 \
      imagemagick libapache-dbi-perl libapache2-mod-perl2 \
      libapache2-mod-wsgi libapache2-mod-svn libapr1-dev libaprutil1-dev \
      libauthen-simple-ldap-perl libcurl4-openssl-dev libdbd-mysql-perl \
      libdbi-perl libio-socket-ssl-perl libmagickcore-dev libmagickwand-dev \
      libmysqlclient-dev libsqlite3-dev libssl-dev make \
      mercurial mysql-client php-mysql ruby ruby-dev ssl-cert subversion \
      supervisor unzip wget && \
    ${ALM_HOME}/install.sh && \
    apt-get clean -y && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt /tmp/*

# Expose web
EXPOSE 80 443

# Define data volumes
VOLUME ["/opt/alminium/files", "/var/opt/alminium", "/var/opt/alminium-backup", "/var/lib/mysql", "/var/log/alminium"]

# supervisor config
COPY ./supervisord.conf /etc/supervisord.conf

# working directory
WORKDIR ${ALM_HOME}

# deamon
ENTRYPOINT /usr/bin/supervisord -c /etc/supervisord.conf

# command
CMD /bin/bash
