FROM phusion/baseimage

MAINTAINER naudster

ENV DEBCONF_NONINTERACTIVE_SEEN="true" DEBIAN_FRONTEND="noninteractive" DISABLESSH="true" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"
ENV SHMEM="50%" TZ="Etc/UTC"

VOLUME ["/config/mysql"]
VOLUME ["/var/cache/zoneminder"]

EXPOSE 80

ADD install.sh /install.sh
ADD firstrun.sh /etc/my_init.d/firstrun.sh
ADD mysql_secure_installation.sql /root/mysql_secure_installation.sql

RUN bash /install.sh

CMD ["/sbin/my_init"]
