FROM openjdk:8-jre-slim

ARG STUBBY_VER
ENV STUBBY_VER ${STUBBY_VER:-5.0.1}
ENV STUBBY_EXTRA ""

RUN apt-get update && \
    apt-get install -y wget && \
    mkdir -p /stubby/config && \
    wget http://central.maven.org/maven2/io/github/azagniotov/stubby4j/${STUBBY_VER}/stubby4j-${STUBBY_VER}.jar -O /stubby/stubby4j-${STUBBY_VER}.jar && \
    apt-get clean && \
    apt autoremove && \
    apt-get purge -y wget && \
    rm -r /var/lib/apt/lists/* \
          /var/log/* \
          /var/cache/debconf/*

COPY stubby.yaml /stubby/config
COPY entrypoint.sh /

VOLUME /stubby/config

ENTRYPOINT ["/entrypoint.sh"]
