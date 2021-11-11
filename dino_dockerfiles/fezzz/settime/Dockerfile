FROM centos:latest
#FROM ubuntu:latest
#MAINTAINER felix@istsotoll.de
#ADD crontab /etc/cron.d/settime-cron
#RUN chmod 0644 /etc/cron.d/settime-cron
#RUN touch /var/log/cron.log
#CMD cron && tail -f /var/log/cron.log

RUN yum update -y; yum clean all
RUN yum install -y openssh-clients cronie sudo epel-release; yum clean all
RUN yum update -y; yum clean all
RUN yum --enablerepo=epel install -y sshpass; yum clean all
RUN sudo echo "KexAlgorithms diffie-hellman-group1-sha1" >> /etc/ssh/ssh_config

#COPY cronjob.txt /etc/crontab
ADD cronjob.txt /etc/crontab
RUN chmod 0644 /etc/crontab
RUN touch /var/log/cron

####RUN /usr/bin/crontab /etc/cron

CMD crond -n

##CMD ["/usr/bin/supervisord"]
