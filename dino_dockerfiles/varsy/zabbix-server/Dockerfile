FROM ubuntu:14.04
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com

ENV TERM=xterm
RUN apt-get -y update && apt-get install -y wget bc sysstat && wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.0-1+trusty_all.deb && \
   dpkg -i zabbix-release_3.0-1+trusty_all.deb

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y zabbix-server-mysql zabbix-frontend-php zabbix-agent zabbix-java-gateway

ADD run-services.sh /
RUN chmod +x /run-services.sh

CMD /run-services.sh
