FROM centos:7

EXPOSE 80
ENTRYPOINT [ "/init" ]

RUN yum -y install epel-release \
        && yum -y install cacti-1.1.28 cronie mod_php php-ldap supervisor \
        && yum -y clean all

COPY docker/ /
