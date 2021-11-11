FROM sathlan/f24-systemd:v1.0.0
LABEL date="Thu Aug 11 18:06:29 CEST 2016"
# based on
# https://github.com/sonatype/docker-nexus3/blob/master/Dockerfile
MAINTAINER <sofer@sathlan.org>

ARG NEXUS_VERSION=3.2.0-01
ARG NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz

RUN dnf install --setopt=tsflags=nodocs -y \
  curl tar net-tools procps-ng \
  && dnf clean all

# configure java runtime
ENV JAVA_HOME=/opt/java \
  JAVA_VERSION_MAJOR=8 \
  JAVA_VERSION_MINOR=112 \
  JAVA_VERSION_BUILD=15

# configure nexus runtime
ENV SONATYPE_DIR=/opt/sonatype
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus \
  NEXUS_DATA=/nexus-data \
  NEXUS_CONTEXT='' \
  SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work

# install Oracle JRE
RUN mkdir -p /opt \
  && curl --fail --silent --location --retry 3 \
  --header "Cookie: oraclelicense=accept-securebackup-cookie; " \
  http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/server-jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
  | gunzip \
  | tar -x -C /opt \
  && ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}

# install nexus
RUN mkdir -p ${NEXUS_HOME} \
  && curl --fail --silent --location --retry 3 \
    ${NEXUS_DOWNLOAD_URL} \
  | gunzip \
  | tar x -C ${NEXUS_HOME} --strip-components=1 nexus-${NEXUS_VERSION} \
  && chown -R root:root ${NEXUS_HOME}

# configure nexus
RUN sed \
    -e '/^nexus-context/ s:$:${NEXUS_CONTEXT}:' \
    -i ${NEXUS_HOME}/etc/nexus-default.properties

# workaround NEXUS-10049 by touching the affected acl.cfg files
RUN touch \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.feature.cfg \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.system.cfg \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.bundle.cfg \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.shell.cfg \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.config.cfg \
    ${NEXUS_HOME}/etc/karaf/org.apache.karaf.command.acl.jaas.cfg

RUN useradd -r -u 200 -m -c "nexus role account" -d ${NEXUS_DATA} -s /bin/false nexus \
  && mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp ${SONATYPE_WORK} \
  && ln -s ${NEXUS_DATA} ${SONATYPE_WORK}/nexus3 \
  && chown -R nexus:nexus ${NEXUS_DATA}

VOLUME ${NEXUS_DATA}

COPY nexus.service /etc/systemd/system/nexus.service
RUN systemctl enable nexus.service

EXPOSE 8081
WORKDIR ${NEXUS_HOME}

ENV JAVA_MAX_MEM=1200m \
  JAVA_MIN_MEM=1200m \
  EXTRA_JAVA_OPTS=""
