FROM centos:latest
MAINTAINER "kev" spam4kev@gmail.com
#
EXPOSE 143 993 25 
#
COPY ./userData.sh /
ENTRYPOINT ["/userData.sh"]
#
RUN yum update -y
RUN yum install -y dovecot \
                   postfix
CMD postfix start && /usr/sbin/dovecot -F -c /etc/dovecot/dovecot.conf
