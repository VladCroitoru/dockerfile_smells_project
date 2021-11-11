FROM openjdk:8u151-jdk-alpine3.7

ARG NEXUS_VERSION=3.8.0-02
#ARG NEXUS_DOWNLOAD_SHA256_HASH=d6605064eae2d6a0679054e3afb039c8b071862644632894e04558e1d067cbfb

# configure nexus runtime
ENV SONATYPE_DIR=/opt/sonatype \
    NEXUS_DATA=/nexus-data
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus \
    NEXUS_CONTEXT='' \
    SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work \
    DOCKER_TYPE='docker' \
    INSTALL4J_ADD_VM_PARAMS="-Xms1200m -Xmx1200m -XX:MaxDirectMemorySize=2g -Djava.util.prefs.userRoot=${NEXUS_DATA}/javaprefs"

RUN apk --update add --no-cache --virtual .build-deps \
    bash \
    tar && \
    wget --quiet https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz -O /tmp/nexus.tar.gz && \
    mkdir /tmp/nexus && \
    tar -xvzf /tmp/nexus.tar.gz -C /tmp/nexus && \
    rm -f /tmp/nexus.tar.gz && \
    mkdir -p ${SONATYPE_WORK} && \
    mv /tmp/nexus/nexus-${NEXUS_VERSION} ${SONATYPE_DIR}/nexus && \
    rm -rf /tmp/nexus && \
    addgroup nexus && \
    adduser -S -s "/bin/false" -u 200 -h ${NEXUS_HOME} -G nexus nexus && \
    chown -R root:root ${SONATYPE_DIR} && \
    chmod -R 755 ${SONATYPE_DIR} && \
    chown -R nexus:nexus ${NEXUS_HOME} && \
    chmod -R 755 ${NEXUS_HOME} && \
    mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp && \
    chown -R root:root ${SONATYPE_WORK} && \
    chmod -R 755 ${SONATYPE_WORK} && \
    ln -s ${NEXUS_DATA} ${SONATYPE_WORK}/nexus3 && \
    chown -R nexus:nexus ${NEXUS_DATA} && \
    chmod -R 755 ${NEXUS_DATA} && \
    apk del .build-deps

VOLUME ${NEXUS_DATA}

EXPOSE 8081
USER nexus

WORKDIR ${NEXUS_HOME}
CMD ["sh", "-c", "exec ./bin/nexus run"]