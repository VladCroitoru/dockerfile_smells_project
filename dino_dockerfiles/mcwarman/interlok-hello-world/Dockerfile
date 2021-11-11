FROM azul/zulu-openjdk-alpine:11-jre

ENV JVM_ARGS=-Xmx1024m
ENV JAVA_OPTS=-Dsun.net.inetaddr.ttl=30
ENV INTERLOK_OPTS=bootstrap.properties
ENV INTERLOK_BASE=/opt/interlok
ENV JAVA_TOOL_OPTIONS=""

RUN apk add --no-cache --update ca-certificates bash curl unzip su-exec && \
    addgroup -S interlok && \
    adduser -S interlok -G interlok && \
    mkdir -p /opt/interlok && \
    chown interlok:interlok /opt/interlok && \
    curl https://raw.githubusercontent.com/adaptris/docker-interlok-base/develop/scripts/suexec-docker-entrypoint.sh -o /docker-entrypoint.sh && \
    chmod +x /docker-entrypoint.sh

COPY --chown=interlok:interlok ./build/distribution /opt/interlok

WORKDIR /opt/interlok/

ENTRYPOINT ["/docker-entrypoint.sh"]
