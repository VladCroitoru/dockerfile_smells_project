FROM centos:centos7

MAINTAINER vdvelde.t@gmail.com

# for systemd
ENV container docker

RUN 	yum -y update && \
 	yum -y install epel-release && \
	yum -y install httpd hostname bind-utils cronie logrotate supervisor && \
	yum -y install openssh openssh-server openssh-client rsyslog sudo passwd sed which pwgen psmisc mailx && \
	yum -y install mariadb-server mariadb-libs mariadb && \
 	yum -y install unzip
RUN 	yum -y install http://packages.icinga.org/epel/7/release/noarch/icinga-rpm-release-7-1.el7.centos.noarch.rpm && \
	yum -y install nagios-plugins-all icinga2 icinga2-doc icinga2-ido-mysql icingaweb2 icingacli php-ZendFramework php-ZendFramework-Db-Adapter-Pdo-Mysql

# docs are not installed by default https://github.com/docker/docker/issues/10650 https://registry.hub.docker.com/_/centos/
# official docs are wrong, go for http://superuser.com/questions/784451/centos-on-docker-how-to-install-doc-files
# we'll need that for mysql schema import for icingaweb2
RUN [ -f /etc/rpm/macros.imgcreate ] && sed -i '/excludedocs/d' /etc/rpm/macros.imgcreate || exit 0
RUN [ -f /etc/yum.conf ] && sed -i '/nodocs/d' /etc/yum.conf || exit 0
RUN yum -y reinstall icingaweb2


# SETUP SSH with no PAM
# http://stackoverflow.com/questions/18173889/cannot-access-centos-sshd-on-docker
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config; \
 echo "sshd: ALL" >> /etc/hosts.allow; \
 rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
 ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
 ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
 echo 'root:yoyo123' | chpasswd; \
 useradd -g wheel appuser; \
 echo 'appuser:appuser' | chpasswd; \
 sed -i -e 's/^\(%wheel\s\+.\+\)/#\1/gi' /etc/sudoers; \
 echo -e '\n%wheel ALL=(ALL) ALL' >> /etc/sudoers; \
 echo -e '\nDefaults:root   !requiretty' >> /etc/sudoers; \
 echo -e '\nDefaults:%wheel !requiretty' >> /etc/sudoers; \
 echo 'syntax on' >> /root/.vimrc; \
 echo 'alias vi="vim"' >> /root/.bash_profile; \
 echo 'syntax on' >> /home/appuser/.vimrc; \
 echo 'alias vi="vim"' >> /home/appuser/.bash_profile;

# fixes at build time (we can't do that at user's runtime)
# setuid problem https://github.com/docker/docker/issues/6828
# 4755 ping is required for icinga user calling check_ping
# can be circumvented for icinga2.cmd w/ mkfifo and chown
# (icinga2 does not re-create the file)
RUN mkdir -p /var/log/supervisor; \
 chmod 4755 /bin/ping /bin/ping6; \
 chown -R icinga:root /etc/icinga2; \
 mkdir -p /etc/icinga2/pki; \
 chown -R icinga:icinga /etc/icinga2/pki; \
 mkdir -p /var/run/icinga2; \
 mkdir -p /var/log/icinga2; \
 chown icinga:icingacmd /var/run/icinga2; \
 chown icinga:icingacmd /var/log/icinga2; \
 mkdir -p /var/run/icinga2/cmd; \
 mkfifo /var/run/icinga2/cmd/icinga2.cmd; \
 chown -R icinga:icingacmd /var/run/icinga2/cmd; \
 chmod 2750 /var/run/icinga2/cmd; \
 chown -R icinga:icinga /var/lib/icinga2; \
 usermod -a -G icingacmd apache >> /dev/null; \
 chown root:icingaweb2 /etc/icingaweb2; \
 chmod 2770 /etc/icingaweb2; \
 mkdir -p /etc/icingaweb2/enabledModules; \
 chown -R apache:icingaweb2 /etc/icingaweb2/*; \
 find /etc/icingaweb2 -type f -name "*.ini" -exec chmod 660 {} \; ; \
 find /etc/icingaweb2 -type d -exec chmod 2770 {} \;

ENV NRDP_TOKEN "token1","token2"
# Setup NRDPE
#ADD $DOWNNRDPE /tmp/nrdp.zip
ADD content/usr/local/nrdp.zip /tmp/
RUN cd /tmp && unzip nrdp.zip && mkdir /usr/local/nrdp/ && cd /usr/local/nrdp/ && cp -r /tmp/nrdp/* . && chown -R apache.apache /usr/local/nrdp && \
    cp /tmp/nrdp/nrdp.conf /etc/httpd/conf.d/ && \
    sed -i '/ Order allow,deny/d' /etc/httpd/conf.d/nrdp.conf && \
    sed -i 's/ Allow from all/Require all granted/g' /etc/httpd/conf.d/nrdp.conf && \
    sed -i 's/\/\/\"mysecrettoken\b.*$/${NRDP_TOKEN}/' /usr/local/nrdp/server/config.inc.php 


# configure PHP timezone
RUN sed -i 's/;date.timezone =/date.timezone = UTC/g' /etc/php.ini

# includes supervisor config
ADD content/ /
RUN chmod +x /usr/local/bin/icinga2_start && chmod +x /usr/local/bin/config-icinga2.sh && chmod +x /usr/local/bin/create_database.sh

# ports (icinga2 api & cluster (5665), mysql (3306))
EXPOSE 22 80 443 5665 3306

# volumes
VOLUME ["/etc/icinga2", "/etc/icingaweb2", "/var/lib/icinga2", "/usr/share/icingaweb2", "/var/lib/mysql"]

ENTRYPOINT ["/usr/local/bin/icinga2_start"]

