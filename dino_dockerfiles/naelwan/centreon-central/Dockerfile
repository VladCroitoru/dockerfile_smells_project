FROM centos:6.7
MAINTAINER naelwan <naelwan@gmail.com>

# Update CentOS
RUN yum -y update

# Install wget
RUN yum install -y wget epel-release

# Get Centreon Repo
RUN wget http://yum.centreon.com/standard/3.0/stable/ces-standard.repo -O /etc/yum.repos.d/ces-standard.repo

# Install Packages (SSH, sudo, Centreon Poller & Engine, SNMP)
RUN yum install -y --nogpgcheck --enablerepo=epel sshpass openssh-clients openssh-server httpd centreon-base-config-centreon-engine centreon sudo net-snmp net-snmp-utils mysql-server
# Add services script
ADD services.sh /etc/
RUN chmod +x /etc/services.sh

# Set timezone
RUN echo "date.timezone = Europe/Paris" > /etc/php.d/php-timezone.ini 

# Change centreon user password
RUN echo -e "password" | (passwd --stdin centreon)

# Disable PAM (causing issues while ssh login)
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# Start services
CMD ["/etc/services.sh"]
