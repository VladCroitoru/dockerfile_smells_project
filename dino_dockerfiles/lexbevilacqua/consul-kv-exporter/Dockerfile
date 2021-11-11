FROM alpine:3.6

RUN apk upgrade --update-cache --available
RUN apk add bash git file
RUN mkdir -p /opt/exporter
WORKDIR /opt/exporter
ADD exporter.sh /opt/exporter/exporter.sh
ADD consul-kv-backup /opt/exporter/consul-kv-backup
RUN chmod 755 /opt/exporter/consul-kv-backup
RUN mkdir /lib64 && cd /lib64 && ln -s /lib/ld-musl-x86_64.so.1 ld-linux-x86-64.so.2
CMD ["bash","/opt/exporter/exporter.sh"]