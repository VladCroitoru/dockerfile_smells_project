FROM centos/systemd

ENV HOME /root
WORKDIR $HOME

#set -e

##Disable Selinux Temporarily
#SELINUX_STATUS=$(getenforce)
#if [ "$SELINUX_STATUS" != "Disabled" ]; then
#    echo "Disabling SELINUX Temporarily"
#    setenforce 0
#else
#  echo "SELINUX it is already disabled"
#fi

##Disable SeLinux Permanently
#sefile="/etc/selinux/config"
#if [ -e $sefile ]
#then
#  sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
#fi

#Install wget command
RUN yum install wget -y

#Clean Yum Cache
RUN yum clean all
RUN rm -rf /var/cache/yum

#Download the beta repo of VitalPBX
RUN rm -rf /etc/yum.repos.d/vitalpbx.repo
RUN wget -P /etc/yum.repos.d/ https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/vitalpbx.repo

#Install SSH Welcome Banner
RUN rm -rf /etc/profile.d/vitalwelcome.sh
RUN wget -P /etc/profile.d/ https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/vitalwelcome.sh
RUN chmod 644 /etc/profile.d/vitalwelcome.sh

#Intall other required dependencies
RUN yum -y install epel-release php

# Update the system & Clean Cache Again
RUN yum clean all
RUN rm -rf /var/cache/yum
RUN yum -y update

#Install MariaDB (MySQL)
RUN yum install mariadb-server -y
RUN systemctl enable mariadb
RUN rm -rf /etc/my.cnf.d/ombutel.cnf
RUN wget -P /etc/my.cnf.d/ https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/ombutel.cnf
RUN systemctl start mariadb

# Install VitalPBX pre-requisites
RUN wget https://raw.githubusercontent.com/VitalPBX/VPS/master/resources/pack_list
RUN yum -y install $(cat pack_list)

# Install VitalPBX
RUN mkdir -p /etc/ombutel
RUN mkdir -p /etc/asterisk/ombutel
RUN yum -y install vitalpbx vitalpbx-asterisk-configs vitalpbx-fail2ban-config vitalpbx-sounds vitalpbx-themes dahdi-linux dahdi-tools dahdi-tools-doc kmod-dahdi-linux fxload

# Speed up the localhost name resolving
RUN sed -i 's/^hosts.*$/hosts:      myhostname files dns/' /etc/nsswitch.conf

#cat << EOF >> /etc/sysctl.d/10-ombutel.conf
## Reboot machine automatically after 20 seconds if it kernel panics
#kernel.panic = 20
#EOF

# Set permissions
RUN chown -R apache:root /etc/asterisk/ombutel

# Restart httpd
RUN systemctl restart httpd

#Start vpbx-setup
RUN systemctl start vpbx-setup.service

# Enable the http access:
RUN firewall-cmd --add-service=http
RUN firewall-cmd --reload

VOLUME /config
VOLUME /var/lib/mysql

EXPOSE 3000/tcp 3005/tcp 3306/tcp

CMD ["/usr/sbin/init"]
