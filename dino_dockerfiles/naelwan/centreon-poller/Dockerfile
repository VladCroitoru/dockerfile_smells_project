FROM centos:6.7
MAINTAINER naelwan <naelwan@gmail.com>

# Update CentOS
RUN yum -y update ; yum clean all

# Install wget
RUN yum install -y wget ; yum clean all

# Get Centreon & EPEL Repos
RUN wget http://yum.centreon.com/standard/3.0/stable/ces-standard.repo -O /etc/yum.repos.d/ces-standard.repo
RUN wget http://epel.mirror.net.in/epel/6/i386/epel-release-6-8.noarch.rpm
RUN rpm -ivh epel-release-6-8.noarch.rpm

# Install Packages (SSH, sudo, Centreon Poller & Engine, SNMP)
RUN yum install -y --nogpgcheck openssh-clients openssh-server centreon-poller-centreon-engine sudo net-snmp net-snmp-utils ; yum clean all
RUN yum install -y sshpass

# Set Timezone
RUN rm -f /etc/localtime
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime


ADD services.sh /etc/
RUN chmod +x /etc/services.sh

ADD plugins/* /usr/lib/nagios/plugins/
RUN chmod 755 /usr/lib/nagios/plugins/check_*_snmp_*
RUN cp /usr/lib64/nagios/plugins/utils.pm /usr/lib/nagios/plugins/


# Change centreon user password
RUN echo "centreon:Password1*" | chpasswd
RUN echo "root:Password1*" | chpasswd


# Disable PAM (causing issues while ssh login)
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# Start services
CMD ["/etc/services.sh"]
