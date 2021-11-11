# Dockerfile for icinga2, icinga-web and icinga2-classicui
FROM debian:stretch
MAINTAINER josh at webhosting coop

# Environment variables
ENV DEBIAN_FRONTEND=noninteractive \
  container=docker \
  ICINGA2_FEATURE_GRAPHITE=true \
  DOCKER_ICINGA2_UPDATED=20181201

# Update package lists.
# Install basic packages.
# Install supervisord because we need to run Apache and Icinga2 at the same time.
# Add debmon repository key to APT.
# Add Debian Backports and Debmon repositories and update package lists again.
# When depencencies are pulled in by icinga-web, they seem to be configured too late and configuration
# of icinga-web fails. To work around this, install dependencies beforehand.
# Clean up some.

# echo "deb http://packages.icinga.org/debian icinga-stretch main" >> /etc/apt/sources.list ; \
# echo "deb-src http://packages.icinga.org/debian icinga-stretch main" >> /etc/apt/sources.list ; \

RUN apt-get -qq update && \
apt-get -qqy install --no-install-recommends gnupg2 sudo procps ca-certificates wget pwgen supervisor && \
wget -O - https://packages.icinga.com/icinga.key | apt-key add - && \
echo "deb http://deb.debian.org/debian stretch-backports main" >> /etc/apt/sources.list  && \
apt-get -qq update  && \
echo "icinga-common icinga/check_external_commands boolean true" | debconf-set-selections
RUN  apt-cache search icinga2
RUN  apt-get install -y -f icinga2
RUN \
apt-get -yqq install \
unzip fail2ban nagios-plugins \
icinga2-bin icinga2-ido-mysql \
icingaweb2 icinga2-classicui \
icinga2 \
mailutils ssmtp icli nagios-plugins-contrib monitoring-plugins openssh-server  && \
dpkg-statoverride --update --add nagios www-data 2710 /var/run/icinga2/cmd/icinga2.cmd  && \
apt-get clean  && \
rm -Rf /var/lib/apt/lists/*

# Add supervisord configuration
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Enable IDO for MySQL. This is needed by icinga-web.
RUN icinga2 feature enable ido-mysql

# create api certificates and users (will be overridden later)
RUN icinga2 api setup

# set icinga2 NodeName and create proper certificates required for the API
RUN sed -i -e 's/^.* NodeName = .*/const NodeName = "docker-icinga2"/gi' /etc/icinga2/constants.conf; \
icinga2 pki new-cert --cn docker-icinga2 --key /etc/icinga2/pki/docker-icinga2.key --csr /etc/icinga2/pki/docker-icinga2.csr; \
icinga2 pki sign-csr --csr /etc/icinga2/pki/docker-icinga2.csr --cert /etc/icinga2/pki/docker-icinga2.crt;

RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config; \
 echo "sshd: ALL" >> /etc/hosts.allow; \
 rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
 ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
 ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
 groupadd wheel && \
 useradd -g wheel appuser && \
 mkdir /home/appuser && \
 chown -R appuser. /home/appuser && \
 sed -i -e 's/^\(%wheel\s\+.\+\)/#\1/gi' /etc/sudoers; \
 echo -e '\n%wheel ALL=(ALL) ALL' >> /etc/sudoers; \
 echo -e '\nDefaults:root   !requiretty' >> /etc/sudoers; \
 echo -e '\nDefaults:%wheel !requiretty' >> /etc/sudoers; \
 echo 'syntax on' >> /root/.vimrc; \
 echo 'alias vi="vim"' >> /root/.bash_profile; \
 echo 'syntax on' >> /home/appuser/.vimrc; \
 echo 'alias vi="vim"' >> /home/appuser/.bash_profile;

#echo 'appuser:appuser' | chpasswd && \
# echo 'root:icingar0xx' | chpasswd && \
# fixes at build time (we can't do that at user's runtime)
# setuid problem https://github.com/docker/docker/issues/6828
# 4755 ping is required for icinga user calling check_ping
# can be circumvented for icinga2.cmd w/ mkfifo and chown
# (icinga2 does not re-create the file)
#RUN mkdir -p /var/log/supervisor; \
 #chmod 4755 /bin/ping /bin/ping6; \
 #chown -R icinga:root /etc/icinga2; \
 #mkdir -p /etc/icinga2/pki; \
 #chown -R icinga:icinga /etc/icinga2/pki; \
 #mkdir -p /var/run/icinga2; \
 #mkdir -p /var/log/icinga2; \
 #chown icinga:icingacmd /var/run/icinga2; \
 #chown icinga:icingacmd /var/log/icinga2; \
 #mkdir -p /var/run/icinga2/cmd; \
 #mkfifo /var/run/icinga2/cmd/icinga2.cmd; \
 #chown -R icinga:icingacmd /var/run/icinga2/cmd; \
 #chmod 2750 /var/run/icinga2/cmd; \
 #chown -R icinga:icinga /var/lib/icinga2; \
 #usermod -a -G icingacmd apache >> /dev/null; \
 #chown root:icingaweb2 /etc/icingaweb2; \
 #chmod 2770 /etc/icingaweb2; \
 #mkdir -p /etc/icingaweb2/enabledModules; \
 #chown -R apache:icingaweb2 /etc/icingaweb2/*; \
 #find /etc/icingaweb2 -type f -name "*.ini" -exec chmod 660 {} \; ; \
 #find /etc/icingaweb2 -type d -exec chmod 2770 {} \;

RUN mkdir -p /var/log/supervisor
# includes supervisor config
ADD content/ /
RUN chmod u+x /opt/icinga2/initdocker

# configure PHP timezone
# RUN sed -i 's/;date.timezone =/date.timezone = UTC/g' /etc/php.ini
#RUN sed -i 's/;date.timezone =/date.timezone = UTC/g' /etc/php7/apache2/php.ini
#RUN sed -i 's/;date.timezone =/date.timezone = UTC/g' /etc/php7/cli/php.ini

# redirect
COPY www/index.html /var/www/html/index.html

# nconf
#RUN ls /usr/share/doc/icinga-idoutils
#COPY nconfinit.sh /tmp/nconfinit.sh
#RUN bash /tmp/nconfinit.sh

#COPY gitmodules.sh /tmp/
#RUN bash /tmp/gitmodules.sh

# ports (icinga2 api & cluster (5665), mysql (3306))
EXPOSE 22 80 443 5665 3306

# volumes
VOLUME ["/etc/icinga2", "/etc/icingaweb2", "/var/lib/icinga2", "/usr/share/icingaweb2", "/var/lib/mysql"]

# change this to entrypoint preventing bash login
# CMD ["/bin/bash"]
CMD ["/opt/icinga2/initdocker"]
#ENTRYPOINT ["/opt/icinga2/initdocker"]
