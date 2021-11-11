FROM alpine:3.12

LABEL maintainer="Gustavo Oliveira <cetres@gmail.com>"

ENV JAVA_HOME=/usr/lib/jvm/default-jvm/jre
ENV PDI_VERSION=7.1 \
    PDI_BUILD=7.1.0.0-12 \
    JRE_HOME=${JAVA_HOME} \
    PENTAHO_JAVA_HOME=${JAVA_HOME} \
    PENTAHO_HOME=/opt/pentaho \
    KETTLE_HOME=/opt/pentaho/data-integration\
    PATH=${PATH}:${JAVA_HOME}/bin

RUN apk update && \
    apk add openjdk8-jre bash webkit2gtk && \
    apk add --virtual build-dependencies ca-certificates openssl && \
    update-ca-certificates && \
    mkdir -p ${PENTAHO_HOME} && \
    wget -qO /tmp/pdi-ce.zip https://downloads.sourceforge.net/project/pentaho/Data%20Integration/${PDI_VERSION}/pdi-ce-${PDI_BUILD}.zip && \
    unzip -q /tmp/pdi-ce.zip -d ${PENTAHO_HOME} && \
    rm -f /tmp/pdi-ce.zip && \
    apk del build-dependencies && \
    chmod -R g+w ${PENTAHO_HOME}

ADD docker-entrypoint.sh $KETTLE_HOME/docker-entrypoint.sh
ADD tests $KETTLE_HOME/

VOLUME ["/opt/pentaho/repository"]
EXPOSE 8080

WORKDIR $KETTLE_HOME
CMD ["/bin/bash", "./docker-entrypoint.sh", "master"]
