FROM centos:latest
MAINTAINER Jonathan Ervine <jon.ervine@gmail.com>

RUN yum update -y &&  yum clean all
RUN yum install -y epel-release
RUN rpm --import http://packages.icinga.org/icinga.key
RUN curl http://packages.icinga.org/epel/ICINGA-release.repo > /etc/yum.repos.d/ICINGA-release.repo
RUN rpm -e --nodeps iputils
RUN yum install -y iputils
RUN yum makecache

VOLUME ["/etc/icinga2", "/etc/icingaweb2", "/var/lib/mysql", "/var/lib/icinga2"]

RUN yum install -y centos-release-scl icinga2 nagios-plugins-all git mariadb-server icinga2-ido-mysql httpd php php-intl php-theseer-fDOMDocument php-gd php-pecl-imagick php-pdo php-ZendFramework-Db-Adapter-Pdo-Mysql supervisor

RUN /usr/libexec/mariadb-prepare-db-dir
RUN /usr/lib/icinga2/prepare-dirs /etc/sysconfig/icinga2
RUN usermod -a -G icingacmd apache
RUN yum install -y icingaweb2 icingacli
##RUN icingacli setup config webserver apache --document-root /usr/share/icingaweb2/public > /etc/httpd/conf.d/icingaweb2.conf

ADD start.sh /sbin/start.sh
RUN chmod 755 /sbin/start.sh
ADD apache.ini /etc/supervisord.d/apache.ini
ADD mariadb.ini /etc/supervisord.d/mariadb.ini
ADD icinga2.ini /etc/supervisord.d/icinga2.ini
ADD php-fm.ini /etc/supervisord.d/php-fm.ini
ADD supervisord.conf /etc/supervisord.conf
#RUN mv /etc/icinga2/conf.d/hosts.conf /etc/icinga2/conf.d/hosts.conf.orig
#RUN mv /etc/icinga2/conf.d/services.conf /etc/icinga2/conf.d/services.conf.orig
#ADD hosts.conf /etc/icinga2/conf.d/hosts.conf
#ADD services.conf /etc/icinga2/conf.d/services.conf

EXPOSE 80 443 5665 9001

ENTRYPOINT ["/sbin/start.sh"]
