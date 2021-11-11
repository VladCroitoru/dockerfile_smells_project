# Version 0.0.2
FROM centos:latest
MAINTAINER Thierry VOGEL <thierry.vogel@moncourriel.eu>
#adaptation de sspreitzer/docker-shellinabox vers centos
#la version 2.14 sspreitzer supporte mal le clavier FR et je prefere centos :p

ENV VERSION 2.18

RUN sed -i '/nodocs/d' /etc/yum.conf
RUN yum -y update && yum -y install openssl curl openssh-client sudo vim tmux  git
RUN yum -y install epel-release && yum -y install supervisor shellinabox 

RUN yum -y install passwd tig

RUN yum clean all && rm -Rf /tmp/* /var/tmp/*

ADD entrypoint.sh /
ADD shellinabox.conf /etc/supervisor/conf.d/
ADD .tmux.conf /etc/skel/
ADD .bashrc /etc/skel/
ADD skel.tgz /etc/skel/

ENV SIAB_USERCSS White On Black:+/usr/share/shellinabox/white-on-black.css,Monochrome:-/usr/share/shellinabox/monochrome.css
ENV SIAB_PORT 4200
ENV SIAB_ADDUSER true
ENV SIAB_USER guest
ENV SIAB_USERID 1000
ENV SIAB_GROUP guest
ENV SIAB_GROUPID 1000
ENV SIAB_PASSWORD putsafepasswordhere
ENV SIAB_SHELL /bin/bash
ENV SIAB_HOME /home/guest
ENV SIAB_SUDO false
ENV SIAB_SSL true
ENV SIAB_SERVICE "/:LOGIN"
ENV SIAB_PKGS none
ENV SIAB_SCRIPT none

EXPOSE 4200

VOLUME /etc/shellinabox
VOLUME /var/log/supervisor
VOLUME /home

ENTRYPOINT ["/entrypoint.sh"]
CMD ["shellinabox"]
