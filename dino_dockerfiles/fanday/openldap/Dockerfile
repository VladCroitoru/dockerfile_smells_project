#
# VERSION               0.0.2
FROM centos:6
MAINTAINER Fanday Dai "fandaydai@live.cn"

#reference:http://www.server-world.info/en/note?os=CentOS_6&p=ldap&f=4
RUN yum -y update
RUN yum -y install wget openldap-servers openldap-clients python-setuptools
RUN cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
RUN chown -R ldap:ldap /var/lib/ldap
ADD files /files
RUN chmod 0755 /files/configure.sh
RUN /bin/bash -l -c '/files/configure.sh'
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -ivh epel-release-6-8.noarch.rpm
RUN rm epel-release-6-8.noarch.rpm
RUN cp /files/supervisord.conf /etc/supervisord.conf
RUN rm -fr /files


RUN yum --enablerepo=epel -y install phpldapadmin

# line 397: uncomment, line 398: comment out
RUN sed -i.bak '397c $servers->setValue('login','attr','dn');' /etc/phpldapadmin/config.php
RUN sed -i.bak '398c //$servers->setValue('login','attr','uid');' /etc/phpldapadmin/config.php

RUN sed -i.bak '10c #Deny from all' /etc/httpd/conf.d/phpldapadmin.conf
RUN sed -i.bak '11c Allow from all' /etc/httpd/conf.d/phpldapadmin.conf

#install suppervisor
RUN easy_install pip
RUN pip install supervisor

RUN sed -i.bak '1c #meld3 >= 0.6.5' /usr/lib/python2.6/site-packages/supervisor-3.1.3-py2.6.egg-info/requires.txt 


EXPOSE 389
EXPOSE 80
EXPOSE 636

CMD ["supervisord","-c", "/etc/supervisord.conf"]

