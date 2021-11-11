# Dockerizing MongoDB Automation Agent
# Based on ubuntu:16.04, installs MongoDB Automation Agent

FROM ubuntu:16.04
MAINTAINER R. Heusser <roland.heusser@sri.com>

ENV REFRESHED_AT 2017-02-27
ENV AGENT_PACKAGE mongodb-mms-automation-agent-manager_latest_amd64.ubuntu1604.deb
ENV AGENT_SOURCE https://cloud.mongodb.com/download/agent/automation/${AGENT_PACKAGE}

# Update
RUN apt-get -qqy update && \
    apt-get install -qqy \
        ca-certificates \
        libsasl2-2

# Download package
ADD ${AGENT_SOURCE} /${AGENT_PACKAGE}

# Installation and permissions
RUN dpkg -i ${AGENT_PACKAGE}
RUN mkdir /data
RUN chown mongodb:mongodb /data

# Mount volumes
VOLUME /etc/mongodb-mms/
VOLUME /data

# Expose Mongo Ports
EXPOSE 27000
EXPOSE 27017

# Set entrypoint when starting image
ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]
