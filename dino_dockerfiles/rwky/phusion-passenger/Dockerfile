FROM phusion/passenger-customizable:0.9.35
MAINTAINER Rowan Wookey <admin@rwky.net>
ENV HOME /root
COPY image/01-syslog-perms.sh /etc/my_init.d/
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5862E31D && \
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0F6DD8135234BF2B && \
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
echo 'deb https://deb.nodesource.com/node_8.x xenial main' > /etc/apt/sources.list.d/nodesource.list && \
echo 'deb-src https://deb.nodesource.com/node_8.x xenial main' >> /etc/apt/sources.list.d/nodesource.list && \
apt-get update && \
apt-get -y purge ntpdate isc-dhcp-common isc-dhcp-client openssh-server openssh-sftp-server && \
apt-get -yq -o Dpkg::Options::="--force-confold" upgrade && \
apt-get -y -o Dpkg::Options::="--force-confold" install tzdata nginx-common nginx-extras passenger passenger-dev passenger-doc && \
rm -rf /etc/my_init.d/00_regen_ssh_host_keys.sh && \
rm -f /etc/nginx/sites-enabled/* && \
rm -rf /etc/service/sshd && \
rm -rf /etc/service/nginx-log-forwarder && \
mkdir -p /etc/service/exim && \
touch /etc/service/exim/down && \
touch /etc/service/nginx/down && \
sed -i 's/rotate 7/rotate 60/' /etc/logrotate.d/syslog-ng && \
sed -i 's@sv reload syslog-ng > /dev/null@kill -HUP \`cat /var/run/syslog-ng.pid\`@' /etc/logrotate.d/syslog-ng && \
chmod +x /etc/my_init.d/01-syslog-perms.sh
COPY image/nginx/* /etc/nginx/conf.d/
COPY image/nginx.conf /etc/nginx/nginx.conf
COPY image/exim.run /etc/service/exim/run
COPY image/nginx.run /etc/service/nginx/run
COPY image/pylogger /usr/local/bin/
COPY image/cron.run /etc/service/cron/run
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
