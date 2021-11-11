FROM centos:centos7
MAINTAINER KrustyHack webmaster@nicolashug.com

ENV ZABBIX_VERSION=3.2.0 \
  ZABBIX_SERVER=127.0.0.1 \
  HOSTNAME= \
  HOST_METADATA=zabbix.agent \
  CONFIG_FILE=/usr/local/etc/zabbix_agentd.conf \
  ZABBIX_PSK=yes

RUN \
  yum clean all && yum makecache && \
  yum install --nogpgcheck -y git svn automake gcc make iproute openssl openssl-devel
RUN \
  svn co svn://svn.zabbix.com/tags/${ZABBIX_VERSION} /usr/local/src/zabbix && \
  cd /usr/local/src/zabbix && \
  ./bootstrap.sh && \
  ./configure --enable-agent --with-openssl && \
  make install
RUN \
  git clone https://github.com/monitoringartist/zabbix-docker-monitoring /tmp/zabbix-docker-monitoring/ && \
  cp -R /tmp/zabbix-docker-monitoring/src/modules/zabbix_module_docker /usr/local/src/zabbix/src/modules/ && \
  cd /usr/local/src/zabbix/src/modules/zabbix_module_docker/ && \
  make
RUN \
  rpm -e --nodeps make gcc && \
  yum remove -y svn automake && \
  useradd -G wheel zabbix && \
  rm -rf  /usr/local/src/zabbix && \
  yum clean all

COPY container-files /

RUN \
  chown -R zabbix:wheel /usr/local/etc/

#USER zabbix

EXPOSE 10050

ENTRYPOINT ["/bootstrap.sh"]
