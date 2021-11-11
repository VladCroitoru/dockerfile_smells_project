FROM phusion/baseimage:0.9.16
MAINTAINER Dejan Lukan <dejan@proteansec.com>

RUN apt-get update
RUN apt-get -y -q install libpcap0.8 unzip

# Install TopBeat
ENV VERSION 1.2.3
ADD https://download.elastic.co/beats/topbeat/topbeat_${VERSION}_amd64.deb .
RUN dpkg -i topbeat_${VERSION}_amd64.deb

# Configuration file
RUN mkdir -p /etc/topbeat/
ADD topbeat.yml /etc/topbeat/topbeat.yml

# entry point takes care of setting conf values
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["app:start"]
