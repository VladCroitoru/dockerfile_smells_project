FROM openjdk:8-jre-alpine

MAINTAINER Said Apale <saidimu@gmail.com>
# Forked from https://hub.docker.com/r/gofly/tranquility/

ENV TRANQUILITY_VERSION=0.8.2
ENV PATH=/opt/tranquility/bin:${PATH}

RUN mkdir -p /opt && \
    apk update && \
    apk add --no-cache bash && \
    apk add --no-cache --virtual .install-deps curl && \
    curl -L http://static.druid.io/tranquility/releases/tranquility-distribution-${TRANQUILITY_VERSION}.tgz | tar -xzf - -C /opt && \
    mv /opt/tranquility-distribution-${TRANQUILITY_VERSION} /opt/tranquility && \
    apk del --purge .install-deps

VOLUME ["/opt/tranquility/conf"]

ENTRYPOINT ["tranquility"]

CMD ["--help"]
# CMD ["server", "-configFile", "/opt/tranquility/conf/server.json"]
# CMD ["kafka", "-configFile", "/opt/tranquility/conf/kafka.json"]
