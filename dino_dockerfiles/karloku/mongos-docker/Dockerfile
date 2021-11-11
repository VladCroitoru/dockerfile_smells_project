FROM        centos:latest
MAINTAINER  Karloku Sang <karloku@loku.it>

COPY        mongodb-org-3.0.repo /etc/yum.repos.d/
RUN         yum update -y && yum install -y mongodb-org

# mkdirs
RUN         mkdir -p /data/db1/log
RUN         mkdir -p /data/db2/log
RUN         mkdir -p /data/configdb/log

# prepare the start script
RUN         mkdir -p ~/scripts
COPY        start.sh ~/scripts/
WORKDIR     ~/scripts
RUN         chmod +x start.sh

EXPOSE      27017
ENTRYPOINT  ["./start.sh"]