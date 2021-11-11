FROM oberthur/docker-generic-app:openjdk-8u131b11

MAINTAINER Kacper Piechota <k.piechota@oberthur.com>

ENV FLYWAY_VERSION 4.2.0

RUN cd /tmp \
    && apt-get update \
    && apt-get install wget \
    && wget https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz \
    && tar -zxvf flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz \
    && mv flyway-${FLYWAY_VERSION} ~/flyway \
    && cd ~ \
    && chown -R app:app flyway \
    && apt-get purge wget \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
    && rm -fr /tmp/* /var/tmp/*
