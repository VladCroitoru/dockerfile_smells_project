FROM ubuntu:20.04
MAINTAINER ian.tibble@netdelta.io 

ARG SITE
ENV SITE ${SITE:-default}
#ARG PORT
#ENV PORT ${PORT:-8000}
ENV DEBIAN_FRONTEND noninteractive

ENV DOCKYARD_SRC=vol_server/nd_base
ENV DOCKYARD_CONFIG=config_base
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/netdelta
ENV DOCKYARD_STAGING=/srv/staging
ENV CONFIG_BASE=/srv/config_base
ENV VENVDIR=/srv/netdelta_venv

#CMD ["/sbin/my_init"]

# Base setup
RUN apt-get update
RUN apt-get install -y apt-utils

RUN apt-get install -q -y curl apache2 libmysqlclient-dev locales && \
    apt-get install -q -y python3.8 tree python3-pip python3.8-dev mysql-client net-tools rsync rabbitmq-server && \
    apt-get install -q -y nmap iputils-ping python3-venv apache2-dev netcat-openbsd vim openssh-server ntpdate

# set system locale - yes, this is necessary
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN rm -rf /var/lib/apt-get/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/www/html/

# configure apache
ADD $DOCKYARD_CONFIG/config/ports.conf /etc/apache2/

RUN echo "ServerName localhost" >> /etc/apache2/conf-enabled/hostname.conf && \
    a2enmod ssl headers proxy proxy_http proxy_html xml2enc rewrite usertrack remoteip && \
    mkdir -p /var/lock/apache2 && \
    mkdir -p /var/run/apache2

# configure runit
#RUN mkdir -p /etc/service/apache
#ADD config/scripts/run_apache.sh /etc/service/apache/run
#ADD config/scripts/init_letsencrypt.sh /etc/my_init.d/
#ADD config/scripts/run_letsencrypt.sh /run_letsencrypt.sh
#RUN chmod +x /*.sh && chmod +x /etc/my_init.d/*.sh 

# Stuff
# Port to expose
#EXPOSE 80 443 ${PORT}
EXPOSE 80 443
#CMD service mysql start && tail -F /var/log/mysql/error.log
RUN mkdir -p /srv/staging
RUN mkdir -p /srv/netdelta_venv
RUN mkdir -p /srv/logs/${SITE}
RUN mkdir -p /data

COPY $DOCKYARD_CONFIG/config/run_web.sh /srv

#COPY ./run_netdelta.sh /srv/staging
VOLUME ["/srv/staging", "/srv/logs", "/srv/netdelta_venv"]
ENTRYPOINT ["/srv/run_web.sh"]
