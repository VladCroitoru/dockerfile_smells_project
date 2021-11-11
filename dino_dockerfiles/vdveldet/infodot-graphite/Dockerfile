FROM centos:centos7

MAINTAINER vdvelde.t@gmail.com

# for systemd
ENV container docker

RUN 	yum -y update && \
 	yum -y install epel-release && \
	yum -y install httpd hostname bind-utils cronie logrotate supervisor && \
	yum -y install rsyslog sudo passwd sed which pwgen psmisc mailx
RUN	yum -y install graphite-web python-carbon


# includes supervisor config
ADD content/ /
RUN chmod +x /usr/local/bin/graphite_start


# Nginx Carbon line receiver Carbon UDP receiver Carbon pickle receiver Carbon cache
expose 80 2003 2003/udp 2004 7002

ENTRYPOINT ["/usr/local/bin/graphite_start"]

