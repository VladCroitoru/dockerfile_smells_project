###
#
# An image for mongodb initialisation using the MMS automation service
#
###
FROM ubuntu:14.04
MAINTAINER Kingsquare <docker@kingsquare.nl>

ENV AGENT_DEB mongodb-mms-automation-agent-manager_1.5.3.873-1_amd64.deb

# MMS-agent volume
VOLUME /var/lib/mongodb-mms-automation
# MongoDB data volume
VOLUME /data
# default MMS automation port
EXPOSE 27000

RUN apt-get -qqy update && \
    apt-get install -qqy --no-install-recommends curl ca-certificates libsasl2-2 && \
    curl -sL "https://mms.mongodb.com/download/agent/automation/${AGENT_DEB}" -o /tmp/automation-agent.deb && \
    dpkg -i /tmp/automation-agent.deb && \
    apt-get clean && \
	rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \
	chown mongodb:mongodb /data

ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]