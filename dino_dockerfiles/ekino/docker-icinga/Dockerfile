FROM debian:7
RUN echo "deb http://ftp2.fr.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list.d/backports.list
RUN apt-get update
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install --assume-yes vim apache2 mysql-server libdbd-mysql mysql-client
RUN apt-get --assume-yes -t wheezy-backports install icinga icinga-cgi icinga-core$ icinga-doc nagios-plugins
RUN sed -i.bak -e s/"command_name\tcheck_https_auth$"/"command_name\tcheck_https_auth_deprecated"/g /etc/nagios-plugins/config/http.cfg
RUN rm -rf /etc/icinga/*
