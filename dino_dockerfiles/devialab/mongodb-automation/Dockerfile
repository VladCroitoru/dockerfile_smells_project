FROM ubuntu:16.04
MAINTAINER Alexander De Leon "alex@devialab.com"

ENV REFRESHED_AT 2021-08-13

RUN apt-get -qqy update && \
    apt-get install -qqy \
        ca-certificates \
        libcurl3 libgssapi-krb5-2 \
        libkrb5-dbg libldap-2.4-2 libpci3 libsasl2-2 snmp \
        liblzma5 openssl
# MMS automation
VOLUME /var/lib/mongodb-mms-automation
ADD https://cloud.mongodb.com/download/agent/automation/mongodb-mms-automation-agent-manager_latest_amd64.ubuntu1604.deb /root/mongodb-mms-automation-agent-manager_latest_amd64.deb
RUN dpkg -i /root/mongodb-mms-automation-agent-manager_latest_amd64.deb

# MongoDB data volume
VOLUME /data
RUN chown mongodb:mongodb /data

# default MMS automation port
EXPOSE 27000

ENTRYPOINT ["/opt/mongodb-mms-automation/bin/mongodb-mms-automation-agent"]
