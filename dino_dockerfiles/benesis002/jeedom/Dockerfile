FROM jeedom/jeedom:latest

MAINTAINER benesis002@outlook.com

RUN apt-get update && apt-get -y dist-upgrade && rm -rf /var/lib/apt/lists && echo "find /var/www/html/plugins -name "*install.sh*" -execdir {} \;" >> /root/init.sh && echo "systemctl stop sshd" >> /root/init.sh
