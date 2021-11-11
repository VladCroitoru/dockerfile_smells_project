FROM centos:centos7

LABEL description "centreon-docker: monitoring systemcatch mail clone jmathis <julien.mathis@gmail.com>"
MAINTAINER maintainer "Manuel Valle <manuvaldi@gmail.com>"

# Update CentOS
RUN yum -y update

# Install Centreon Repository
RUN yum -y install http://yum.centreon.com/standard/3.4/el7/stable/noarch/RPMS/centreon-release-3.4-4.el7.centos.noarch.rpm

# Install ssh
RUN yum -y install openssh-server openssh-client
RUN mkdir /var/run/sshd
RUN echo 'root:centreon' | chpasswd
RUN sed -i 's/^#PermitRootLogin/PermitRootLogin/g' /etc/ssh/sshd_config
#RUN /etc/init.d/sshd start && /etc/init.d/sshd stop

# Install centreon
RUN yum -y install MariaDB-server && /etc/init.d/mysql start && yum -y install centreon centreon-base-config-centreon-engine centreon-installed centreon-clapi && /etc/init.d/mysql stop

# Install plugins
RUN yum -y install nagios-plugins-tcp nagios-plugins-ssh nagios-plugins-fping

# setting php
RUN sed -i  's/;date.timezone =/date.timezone =UTC/' /etc/php.ini

# Install Widgets
RUN yum -y install centreon-widget-graph-monitoring centreon-widget-host-monitoring centreon-widget-service-monitoring centreon-widget-hostgroup-monitoring centreon-widget-servicegroup-monitoring

# Fix pass in db
ADD scripts/cbmod.sql /tmp/cbmod.sql
RUN /etc/init.d/mysql start && sleep 5 && mysql centreon < /tmp/cbmod.sql && /usr/bin/centreon -u admin -p centreon -a POLLERGENERATE -v 1 && /usr/bin/centreon -u admin -p centreon -a CFGMOVE -v 1 && /etc/init.d/mysql stop

# Set rights for setuid
RUN chown root:centreon-engine /usr/lib/nagios/plugins/check_icmp
RUN chmod -w /usr/lib/nagios/plugins/check_icmp
RUN chmod u+s /usr/lib/nagios/plugins/check_icmp


# Install and configure supervisor
RUN yum -y install python-setuptools
RUN easy_install supervisor

# Todo better split file
ADD scripts/supervisord.conf /etc/supervisord.conf
ADD scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port SSH and HTTP for the service
EXPOSE 22 80

RUN cp -Rp /var/lib/mysql /var/lib/mysql.original  \
  && cp -Rp /etc/centreon /etc/centreon.original \
  && cp -Rp /etc/centreon-engine /etc/centreon-engine.original \
  && cp -Rp /etc/centreon-broker /etc/centreon-broker.original

VOLUME ["/var/backup","/var/lib/mysql","/etc/centreon","/etc/centreon-engine","/etc/centreon-broker"]

ENTRYPOINT ["/entrypoint.sh"]
#CMD ["/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]
