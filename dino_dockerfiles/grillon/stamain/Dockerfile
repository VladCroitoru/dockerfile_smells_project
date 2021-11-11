# Version 0.0.2
FROM centos:latest
MAINTAINER Thierry VOGEL <thierry.vogel@moncourriel.eu>
#env de maintenance applicative

#edition
RUN sed -i '/nodocs/d' /etc/yum.conf
RUN yum -y update 
RUN yum -y install epel-release
RUN yum -y install curl vim tmux git tig ctags

#supervisor
RUN yum -y install supervisor openssh-server openssh-client telnet passwd sudo


RUN yum clean all && rm -Rf /tmp/* /var/tmp/*


#home
ADD .tmux.conf /etc/skel/
ADD .bashrc /etc/skel/
ADD skel.tgz /etc/skel/

ENV STAMAIN_PUID thierry 1000 1000
ENV STAMAIN_PGID thierry 1000
ENV STAMAIN_PASSWD mdpQuiCraint

#conf supervisor
RUN ssh-keygen -A
RUN mkdir -p /var/run/sshd /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD prepare.sh /

EXPOSE 22

VOLUME /var/log/supervisor
VOLUME /home

ENTRYPOINT ["/prepare.sh"]
CMD ["ssh"]
