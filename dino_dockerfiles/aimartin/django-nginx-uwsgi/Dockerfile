FROM centos

MAINTAINER Aitor Martin <aitor@martinh.es>

ENV HOME /root

ADD epel.repo /etc/yum.repos.d/epel.repo

ADD epel.key /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

ADD nginx.repo /etc/yum.repos.d/nginx.repo

RUN yum clean all

RUN yum install -y libjpeg-devel zlib-devel openldap-devel mariadb-devel python-ldap python-devel python-setuptools gcc hg nginx

RUN rm /etc/nginx/conf.d/*

ADD nginx.conf /etc/nginx/nginx.conf

ADD nginx-syslog.conf /etc/nginx/nginx-syslog.conf

RUN easy_install virtualenv uwsgi

ADD init.sh /usr/bin/init.sh

CMD /usr/bin/init.sh

EXPOSE 80 443

VOLUME ["/var/www"]
