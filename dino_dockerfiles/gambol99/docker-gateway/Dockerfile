#
#   Author: Rohith (gambol99@gmail.com)
#   Date: 2015-01-26 16:17:44 +0000 (Mon, 26 Jan 2015)
#
#  vim:ts=2:sw=2:et
#
FROM centos:latest
MAINTAINER Rohith <gambol99@gmail.com>

ADD config/sshd.ini /etc/supervisord.d/sshd.ini
ADD config/sshd_config /etc/ssh/sshd_config
ADD config/authorized_keys /root/.ssh/authorized_keys

# install epel repository
RUN yum install -y http://mirrors.coreix.net/fedora-epel/7/x86_64/e/epel-release-7-5.noarch.rpm
# install ssh and supervisord
RUN yum install -y openssh-server supervisor
# install some tools
RUN yum install -y httpd-tools nmap nc telnet iftop siege tar wget bzip2 mysql vim openssh-clients git docker
# ensure the permissions
RUN chmod 0400 /root/.ssh/authorized_keys && chown root:root /root/.ssh/authorized_keys

# expose ssh
EXPOSE 22

ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n" ]
