FROM alpine:3.3

ENV AB_VERSION="0.1.2" \
  AB_HOME="/opt/agent-bond"

RUN set -x && \
  apk add --update bash curl ca-certificates openjdk8-jre-base && \
  rm /var/cache/apk/*

RUN set -x && \
  mkdir -p $AB_HOME && \
  curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-pepper/agent-bond/fp-files/agent-bond-opts  -o /usr/local/bin/agent-bond-opts && \
  sed -i 's|/bin/sh|/bin/bash|g' /usr/local/bin/agent-bond-opts && \
  chmod 755 /usr/local/bin/agent-bond-opts && \
  curl -sSL http://central.maven.org/maven2/io/fabric8/agent-bond-agent/${AB_VERSION}/agent-bond-agent-${AB_VERSION}.jar -o $AB_HOME/agent-bond.jar && \
  chmod 444 $AB_HOME/agent-bond.jar && \
  curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-pepper/agent-bond/fp-files/jmx_exporter_config.json -o $AB_HOME/jmx_exporter_config.json && \
  chmod 444 $AB_HOME/jmx_exporter_config.json

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8778 9779

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["java","-version"]
