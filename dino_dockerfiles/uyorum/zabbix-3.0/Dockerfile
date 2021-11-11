FROM monitoringartist/zabbix-xxl:latest

MAINTAINER uyorum uyorum.pub@gmail.com

COPY api /etc/zabbix/api/uyorum
ADD https://raw.githubusercontent.com/uyorum/zabbix-alert-slack/master/slack \
      /usr/local/share/zabbix/alertscripts/slack
