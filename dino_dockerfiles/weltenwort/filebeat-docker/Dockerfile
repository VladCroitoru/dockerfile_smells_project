FROM alpine:3.5

ARG FILEBEAT_VERSION=5.1.1

ADD https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz /tmp/filebeat.tar.gz
RUN tar -C /tmp -xzf /tmp/filebeat.tar.gz \
 && mv /tmp/filebeat-${FILEBEAT_VERSION}-linux-x86_64/ /usr/share/filebeat/ \
 && true

ENTRYPOINT ["/usr/share/filebeat/filebeat"]
