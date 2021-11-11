FROM debian:jessie

RUN apt-get update && apt-get install -y wget logrotate && rm -rf /var/lib/apt/lists/*

ENV MMS_VERSION 2.9.0.1764-1

# see https://mms.mongodb.com/settings/monitoring-agent
# click on "Ubuntu 12.04+"
RUN wget -O mms.deb "https://cloud.mongodb.com/download/agent/automation/mongodb-mms-automation-agent-manager_${MMS_VERSION}_$(dpkg --print-architecture).ubuntu1604.deb" \
	&& dpkg -i mms.deb \
	&& rm mms.deb

# missing dep in mms.deb
RUN apt-get update && apt-get install -y libsasl2-2 && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["/bin/bash", "/usr/local/bin/docker-entrypoint.sh"]

USER mongodb
CMD ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent", "-f", "/etc/mongodb-mms/automation-agent.config"]