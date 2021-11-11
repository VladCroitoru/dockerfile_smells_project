FROM centos:centos6

# https://hub.docker.com/u/kawanamiyuu
MAINTAINER kawanamiyuu

# install basic packages
RUN yum install -y wget tar gcc

# set timezone
RUN rm -f /etc/localtime
RUN ln -s /usr/share/zoneinfo/UTC /etc/localtime

# install supervisord
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum --enablerepo=epel install -y supervisor
RUN mv -f /etc/supervisord.conf /etc/supervisord.conf.org
ADD supervisord.conf /etc/

# install rsyslogd
RUN yum install -y rsyslog

# install crond
RUN yum install -y cronie-noanacron
# no PAM
RUN cp -a /etc/pam.d/crond /etc/pam.d/crond.org
RUN sed -i -e 's/^\(session\s\+required\s\+pam_loginuid\.so\)/#\1/' /etc/pam.d/crond

# install sshd
RUN yum install -y openssh-server sudo
# no PAM
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN sed -i -e 's/^\(UsePAM\s\+.\+\)/#\1/gi' /etc/ssh/sshd_config
RUN echo -e '\nUsePAM no' >> /etc/ssh/sshd_config

RUN echo 'root:root' | chpasswd
# no direct ROOT login
RUN sed -i -e 's/^\(PermitRootLogin\s\+.\+\)/#\1/gi' /etc/ssh/sshd_config
RUN echo -e '\nPermitRootLogin no' >> /etc/ssh/sshd_config

RUN useradd -g wheel appuser
RUN echo 'appuser:appuser' | chpasswd
RUN sed -i -e 's/^\(%wheel\s\+.\+\)/#\1/gi' /etc/sudoers
RUN echo -e '\n%wheel ALL=(ALL) ALL' >> /etc/sudoers

# allow sudo without tty for ROOT user and WHEEL group
# http://qiita.com/ryo0301/items/4daf5a6d22f16193410f
RUN echo -e '\nDefaults:root   !requiretty' >> /etc/sudoers
RUN echo -e '\nDefaults:%wheel !requiretty' >> /etc/sudoers

# for sshd
EXPOSE 22

# ENTRYPOINT ["/usr/bin/supervisord"] does not work.
# --> "Error: positional arguments are not supported"
# http://stackoverflow.com/questions/22465003/error-positional-arguments-are-not-supported
CMD ["/usr/bin/supervisord"]

# install vim
RUN yum install -y vim
# for root
RUN echo 'syntax on'      >> /root/.vimrc
RUN echo 'alias vi="vim"' >> /root/.bash_profile
# for appuser
RUN echo 'syntax on'      >> /home/appuser/.vimrc
RUN echo 'alias vi="vim"' >> /home/appuser/.bash_profile
