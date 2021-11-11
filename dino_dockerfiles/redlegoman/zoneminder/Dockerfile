# This is a comment
FROM ubuntu:16.04
MAINTAINER Andy McDade (redlegoman) 
LABEL Description="Zoneminder 1.30 in an Ubuntu 16.04 system which runs systemd. Some values in the zoneminder database have been changed already so this should run out of the box."
LABEL Version="1.0"
RUN echo "root:root" | chpasswd
RUN find /etc/systemd/system \
         /lib/systemd/system \
         -path '*.wants/*' \
         -not -name '*journald*' \
         -not -name '*systemd-tmpfiles*' \
         -not -name '*systemd-user-sessions*' \
         -exec rm \{} \;

RUN systemctl set-default multi-user.target
RUN apt-get update && apt-get install -y apt-utils 
RUN apt-get install -y ssh vim
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

RUN apt-get install -y software-properties-common python-software-properties 
RUN add-apt-repository -u -y ppa:iconnor/zoneminder 
RUN add-apt-repository -u -y ppa:jonathonf/ffmpeg-3 

ENV MYSQL_ROOT_PASSWORD=root
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections && \
		echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections && \
		apt-get update && apt-get -y install mysql-server

RUN apt-get update && apt-get install -y apache2 wget php libapache2-mod-php 
RUN apt-get update && apt-get install -y zoneminder libvlc-dev libvlccore-dev vlc ffmpeg 
RUN a2enmod cgi
RUN a2enmod rewrite
RUN a2enconf zoneminder

RUN sed -i 's/;date.timezone =/date.timezone = Europe\/London/g' /etc/php/7.0/apache2/php.ini 

COPY setup /sbin/
COPY rc.local /etc/
COPY firstrun.sh /usr/local/sbin/

VOLUME ["/var/lib/mysql"]
VOLUME ["/var/cache/zoneminder"]
VOLUME ["/usr/share/zoneminder"]

CMD ["/sbin/init"]

