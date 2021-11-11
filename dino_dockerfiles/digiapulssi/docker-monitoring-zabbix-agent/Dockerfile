##################################
# docker-monitoring-zabbix-agent #
##################################
FROM centos:7
COPY data /data
WORKDIR /data
RUN rpm -ivh http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-release-3.2-1.el7.noarch.rpm && \
  yum install -y zabbix-agent docker sudo && \ 
  yum clean all && \
  chmod 0750 /data/start.sh /data/discover.py && \
  chown -R zabbix /data 
VOLUME ["/var/run/docker.sock"]
CMD ["/data/start.sh"]
