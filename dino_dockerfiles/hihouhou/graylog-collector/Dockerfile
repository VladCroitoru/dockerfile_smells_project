#
# Graylog collector Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV COLLECTOR_VERSION graylog-collector-0.4.2

# Update & install packages for graylog
RUN apt-get update && \
    apt-get install -y wget dpkg-dev openjdk-7-jre
RUN wget https://packages.graylog2.org/releases/graylog-collector/${COLLECTOR_VERSION}.tgz && \
    tar xvf ${COLLECTOR_VERSION}.tgz

#Configure graylog
ADD collector.conf /${COLLECTOR_VERSION}/config/

WORKDIR /${COLLECTOR_VERSION}

CMD ["bin/graylog-collector", "run", "-f", "config/collector.conf"]
