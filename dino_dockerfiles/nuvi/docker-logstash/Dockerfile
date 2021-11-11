FROM ubuntu:16.04

ENV LOGSTASH_VERSION 6.2.3
ENV LOGSTASH_EXPORTER_VERSION 0.1.2

RUN apt update && apt install curl wget default-jdk -y
# Install logstash
RUN cd /tmp && wget https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.deb && dpkg -i logstash-${LOGSTASH_VERSION}.deb && rm ./logstash-${LOGSTASH_VERSION}.deb

# Install logstash-exporter
RUN cd /tmp && wget https://github.com/nuvi/logstash_exporter/releases/download/v${LOGSTASH_EXPORTER_VERSION}/logstash_exporter_${LOGSTASH_EXPORTER_VERSION}_linux_amd64.tar.gz && \
  tar -zxvf logstash_exporter_${LOGSTASH_EXPORTER_VERSION}_linux_amd64.tar.gz && \
  mv /tmp/logstash-exporter /usr/local/bin/logstash-exporter && \
  rm logstash_exporter_${LOGSTASH_EXPORTER_VERSION}_linux_amd64.tar.gz

EXPOSE 9198

