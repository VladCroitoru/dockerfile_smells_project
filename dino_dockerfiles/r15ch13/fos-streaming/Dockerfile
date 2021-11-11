FROM phusion/baseimage:0.9.18
MAINTAINER r15ch13 <r15ch13+git@gmail.com>
ENV DEBIAN_FRONTEND=noninteractive

ENV PROVISION_DIR=${PROVISION_DIR:-/provision}
ENV FOS_HOME_DIR=${FOS_HOME_DIR:-/home/fos-streaming}
ENV FOS_GIT_DIR=${FOS_GIT_DIR:-$FOS_HOME_DIR/fos-streaming.git}
ENV FOS_INSTALL_DIR=${FOS_INSTALL_DIR:-$FOS_HOME_DIR/fos-streaming}
ENV FOS_USER=${FOS_USER:-fosstreaming}
ENV FOS_HLS_CACHE=${FOS_HLS_CACHE:-/hls-cache}

ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD:-fosstreaming}
ENV MYSQL_DATABASE=${MYSQL_DATABASE:-fosstreaming}
ENV MYSQL_USERNAME=${MYSQL_USERNAME:-fosstreaming}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD:-fosstreaming}

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# User
RUN sudo useradd -s /sbin/nologin -U -d $FOS_HOME_DIR -m $FOS_USER
RUN sudo sh -c 'echo "nameserver 8.8.8.8" >> /etc/resolv.conf'

# Installing Stuff
RUN sudo apt-get update > /dev/null 2>&1
RUN sudo apt-get install -y wget curl git make build-essential unzip openssl librtmp0 librtmp-dev libjpeg8 > /dev/null 2>&1

ADD /provision $PROVISION_DIR
RUN . $PROVISION_DIR/nginx.sh
RUN . $PROVISION_DIR/php.sh
RUN . $PROVISION_DIR/repo.sh
RUN . $PROVISION_DIR/ffmpeg.sh
RUN . $PROVISION_DIR/mariadb.sh
RUN . $PROVISION_DIR/final.sh

RUN mkdir -p /etc/service/mysql
ADD $PROVISION_DIR/config/mysql.sh /etc/service/mysql/run
RUN sudo chmod 755 /etc/service/mysql/run
RUN mkdir -p /etc/service/php5-fpm
ADD $PROVISION_DIR/config/php5-fpm.sh /etc/service/php5-fpm/run
RUN sudo chmod 755 /etc/service/php5-fpm/run
RUN mkdir -p /etc/service/nginx
ADD $PROVISION_DIR/config/nginx.sh /etc/service/nginx/run
RUN sudo chmod 755 /etc/service/nginx/run
RUN ls -lR /etc/service/

# CronJob
RUN sudo FOS_INSTALL_DIR=$FOS_INSTALL_DIR sh -c 'echo "*/2 * * * * fosstreaming php $FOS_INSTALL_DIR/cron.php" >> /etc/crontab'

VOLUME $FOS_HLS_CACHE
EXPOSE 80

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
