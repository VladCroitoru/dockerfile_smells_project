# Base on latest CentOS image
FROM centos:latest

MAINTAINER “Jon Ervine” <jon.ervine@gmail.com>
ENV container docker

# Install updates and some dev tools
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y supervisor dialog git iproute net-tools newt procps-ng bc bind-utils cronie curl dnsmasq findutils nmap-ncat sudo unzip wget libidn2 psmisc lighttpd lighttpd-fastcgi php php-common php-cli php-pdo
RUN yum clean all
RUN rm -rf /var/cache/yum

ADD start.sh /sbin/start.sh
ADD docker-install.sh /tmp/docker-install.sh
ADD dnsmasq.ini /etc/supervisord.d/dnsmasq.ini
ADD lighttpd.ini /etc/supervisord.d/lighttpd.ini
ADD pihole.ini /etc/supervisord.d/pihole.ini
ADD supervisord.conf /etc/supervisord.conf
RUN chmod 755 /sbin/start.sh

EXPOSE 53 80

ENTRYPOINT ["/sbin/start.sh"]
