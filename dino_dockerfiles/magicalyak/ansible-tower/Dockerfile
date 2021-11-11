#                      _           _          _    
#    /\/\   __ _  __ _(_) ___ __ _| /\_/\__ _| | __
#   /    \ / _` |/ _` | |/ __/ _` | \_ _/ _` | |/ /
#  / /\/\ \ (_| | (_| | | (_| (_| | |/ \ (_| |   < 
#  \/    \/\__,_|\__, |_|\___\__,_|_|\_/\__,_|_|\_\
#                |___/                             

FROM ansible/centos7-ansible
MAINTAINER "magicalyak" <tom.gamull@gmail.com>

# global environment settings
ENV SERVER_NAME localhost
ENV ADMIN_PASSWORD changeme
ENV ANSIBLE_TOWER_VER latest

ADD ./inventory /opt/inventory
ADD ./ansible-setup.service /opt/ansible-setup.service
ADD ./docker-entrypoint.sh /docker-entrypoint.sh

RUN \
# Set systemd
 yum -y update; yum clean all; \
 (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
 rm -f /lib/systemd/system/multi-user.target.wants/*;\
 rm -f /etc/systemd/system/*.wants/*;\
 rm -f /lib/systemd/system/local-fs.target.wants/*; \
 rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
 rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
 rm -f /lib/systemd/system/basic.target.wants/*; \
 rm -f /lib/systemd/system/anaconda.target.wants/*; \
# install Ansible
 yum makecache fast && \
 yum -y install deltarpm epel-release initscripts && \
 yum -y update && \
 yum -y install ansible sudo which wget && \

# add passwords and fix locale issue
 cd /opt && \
 sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers && \
 echo "Setting password to $ADMIN_PASSWORD" && \
 sed -i "s/changeme/$ADMIN_PASSWORD/g" /opt/inventory && \
 echo "Setting connection to $SERVER_NAME" && \
 echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts && \
 echo "Setting rebuild flag in /certs in case it isn't mapped" && \
 mkdir -p /certs/.deleteme && \
 touch /certs/.rebuild && \

# cleanup
 echo "Cleaning up...." && \
 yum clean all && \
 rm -rf \
        /tmp/* \
        /var/tmp/*

# ports and volumes
EXPOSE 443 8080
VOLUME /sys/fs/cgroup /var/lib/pgsql/9.4/data /certs

# set runtime options for ansibkle-setup
RUN echo "Setting up ansible-setup service to run at boot" && \
    echo "# ansible-setup.env" > /opt/ansible-setup.env && \
    echo "SERVER_NAME=$SERVER_NAME" >> /opt/ansible-setup.env && \
    echo "ANSIBLE_TOWER_VER=$ANSIBLE_TOWER_VER" >> /opt/ansible-setup.env && \
    echo "ADMIN_PASSWORD=$ADMIN_PASSWORD" >> /opt/ansible-setup.env && \
    chmod +x /docker-entrypoint.sh && \
    cp /opt/ansible-setup.service /etc/systemd/system/ansible-setup.service && \
    systemctl enable ansible-setup.service

CMD [ "/usr/sbin/init" ]
