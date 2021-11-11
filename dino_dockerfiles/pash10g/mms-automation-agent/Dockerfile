FROM ubuntu:16.04
MAINTAINER pavel duchovny "pavel.duchovny@mongodb.com"

RUN apt-get -qqy update && \
    apt-get install -qqy \
        curl \
        ca-certificates \
        libsasl2-2 \
        numactl


#VOLUME /var/lib/mongodb-mms-automation
ENV MMS_URL "https://cloud.mongodb.com"
ARG MMS_URL
ADD $MMS_URL/download/agent/automation/mongodb-mms-automation-agent-manager_latest_amd64.deb /root/mongodb-mms-automation-agent-manager_latest_amd64.deb

RUN dpkg -i /root/mongodb-mms-automation-agent-manager_latest_amd64.deb

#Setting /var/lib permissions
RUN chmod -R 777 /var/lib/


# MMS automation
# MongoDB data volume
VOLUME /data
RUN chown -R mongodb:mongodb /data
USER mongodb

# default MMS automation port
EXPOSE 27000

ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]
#ENTRYPOINT ["/entrypoint.sh"]
