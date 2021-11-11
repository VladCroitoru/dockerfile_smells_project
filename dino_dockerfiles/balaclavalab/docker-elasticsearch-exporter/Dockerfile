FROM alpine:3.10

RUN set -x \
  && apk add --no-cache wget ca-certificates \
  && update-ca-certificates \
  && wget https://github.com/echocat/elasticsearch_exporter/releases/download/v0.3.0-echocat-1/elasticsearch_exporter-linux-amd64 \
          -O /usr/local/bin/elasticsearch_exporter \
  && chmod +x /usr/local/bin/elasticsearch_exporter

EXPOSE 9108

ENTRYPOINT ["/usr/local/bin/elasticsearch_exporter"]
