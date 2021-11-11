FROM ubuntu

MAINTAINER "SeaLife" <sealife@r3ktm8.de>

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y apache2 php7.0 php7.0-common mysql-client php7.0-mcrypt php7.0-mbstring
RUN apt-get install -y libapache2-mod-php7.0
RUN apt-get install -y git
RUN apt-get install -y php7.0-mysql
RUN apt-get install -y cron
RUN apt-get install -y curl php7.0-curl wget

COPY start.sh /
COPY cron-monitoring /etc/cron.d/cron-monitoring
COPY init.sh /
COPY dir.conf /etc/apache2/sites-enabled/dir.conf
COPY monitoring.sh /

EXPOSE 80

ENTRYPOINT ["/init.sh"]
