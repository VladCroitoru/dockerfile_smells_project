FROM debian:wheezy
MAINTAINER Alex Anghelone <alex.anghelone@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

ADD supervisord/apache2.conf /etc/supervisor/conf.d/apache2.conf
ADD supervisord/percona.conf /etc/supervisor/conf.d/percona.conf
ADD scripts/postBuildTasks.sh /root/bin/postBuildTasks.sh
ADD scripts/run.sh /root/bin/run.sh


RUN sed -i 's/main/main\ contrib\ non-free/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y -q wget

ADD apt/percona.list /etc/apt/sources.list.d/percona.list
ADD apt/dotdeb.list /etc/apt/sources.list.d/dotdeb.list

RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A
RUN wget -O /root/dotdeb.gpg http://www.dotdeb.org/dotdeb.gpg && apt-key add /root/dotdeb.gpg
RUN apt-get update
RUN apt-get -q -y install percona-server-server-5.6 percona-server-client-5.6 percona-toolkit apache2 php5 php5-mysql libapache2-mod-php5 supervisor pwgen
RUN a2enmod rewrite
RUN a2enmod php5
RUN update-rc.d -f apache2 remove
RUN update-rc.d -f mysql remove

VOLUME  ["/etc/apache2/", "/etc/mysql", "/var/lib/mysql" ]

EXPOSE 80 3306

RUN chmod 755 /root/bin/*.sh

CMD ["/root/bin/run.sh"]
