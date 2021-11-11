FROM adoptopenjdk/openjdk8:x86_64-alpine-jdk8u212-b04

ENV NEXUS_OSS_VERSION 3.21.1-01

RUN addgroup -g 10777 worker && \
    adduser -h /work -H -D -G worker -u 10777 worker && \
    mkdir -p /work && \
    mkdir -p /opt && \
    mkdir -p /work-private && \
    mkdir /nexus && mkdir /nexus-home && \
    chown -R worker:worker /work/ && \
    chown -R worker:worker /work-private/ && \
    apk add --no-cache \
            ca-certificates \
            bash \
            curl \
            tar \
            python \
            py-pip && \
            pip install shinto-cli && \
    curl -jkSL -o /opt/nexus-${NEXUS_OSS_VERSION}-unix.tar.gz \
         https://sonatype-download.global.ssl.fastly.net/repository/repositoryManager/3/nexus-${NEXUS_OSS_VERSION}-unix.tar.gz && \
    cd /opt && \
    tar zxf /opt/nexus-${NEXUS_OSS_VERSION}-unix.tar.gz -C /nexus && \
    rm /opt/nexus-${NEXUS_OSS_VERSION}-unix.tar.gz && \
    cd /nexus && \
    ln -s nexus-${NEXUS_OSS_VERSION} nexus-latest && \
    chown -R worker:worker /nexus && \
    chown -R worker:worker /nexus-home/

#
# FILES
#
COPY docker-entrypoint.sh /work-private/docker-entrypoint.sh
RUN chmod u+rx,g+rx,o+rx,a-w /work-private/docker-entrypoint.sh && \
    chown -R worker:worker /work-private/

#
# WORKDIR
#
WORKDIR /work
EXPOSE 8443

#
# k8s readiness exec probe cmd
#
COPY k8s-readiness-probe.sh /work-private/k8s-readiness-probe.sh
RUN chmod u+rx,g+rx,o+rx,a-w /work-private/k8s-readiness-probe.sh

#
# RUN
#
USER worker
ENV NEXUS_OSS_BASE /nexus-home
ENV NEXUS_DOMAIN localhost
ENV NEXUS_IP_ADDRESS 127.0.0.1
VOLUME ["/work"]
VOLUME ["/nexus-home"]
ENTRYPOINT ["/work-private/docker-entrypoint.sh"]
CMD ["/nexus/nexus-latest/bin/nexus", "run"]
