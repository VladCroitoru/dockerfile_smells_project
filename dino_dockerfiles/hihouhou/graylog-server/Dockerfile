#
# Graylog server Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV SERVER_VERSION graylog-2.0.0
ENV ES_VERSION elasticsearch-2.3.0

# Update & install packages for graylog
RUN apt-get update && \
    apt-get install -y wget dpkg-dev openjdk-7-jre
RUN wget https://packages.graylog2.org/releases/graylog/$SERVER_VERSION.tgz && \
    tar xvf $SERVER_VERSION.tgz && \
    mkdir -p /etc/graylog/server/

#Configure graylog
ADD server.conf /etc/graylog/server/

#Configure ES
RUN wget https://download.elastic.co/elasticsearch/elasticsearch/$ES_VERSION.deb && \
 dpkg -i $ES_VERSION.deb

#Add link for binary
RUN ln -s /$SERVER_VERSION/bin/graylogctl /usr/bin/graylogctl && ls -l /usr/bin/graylogctl

EXPOSE 12900

CMD ["graylogctl", "run"]
