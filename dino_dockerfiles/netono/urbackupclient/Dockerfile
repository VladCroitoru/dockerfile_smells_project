FROM ubuntu:14.04

RUN mkdir /backup
RUN apt-get update && apt-get install -y wget

COPY start.sh /opt/start.sh
COPY urbackupclient /opt/urbackupclient
RUN chmod +x /opt/start.sh