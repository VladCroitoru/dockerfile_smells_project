FROM debian:jessie
MAINTAINER it-operations@boerse-go.de

ADD http://repo.zabbix.com/zabbix-official-repo.key /tmp/
RUN echo "deb http://repo.zabbix.com/zabbix/3.2/debian jessie main" > /etc/apt/sources.list.d/zabbix.list && \
    apt-key add - < /tmp/zabbix-official-repo.key && \
    rm /tmp/zabbix-official-repo.key && \
    apt-get update -y && \
    apt-get install -y zabbix-agent && \
    apt-get clean && rm -r /var/lib/apt/lists/* && \
    /bin/mkdir -p /run/zabbix && \
    /bin/chown -R zabbix:zabbix /run/zabbix
ADD entrypoint.sh /

EXPOSE 10050

CMD [ "/entrypoint.sh" ]
#CMD ["/bin/bash"]
