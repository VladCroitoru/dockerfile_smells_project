FROM       centos:centos7
MAINTAINER Flávio Lisbôa <flisboa.costa@gmail.com>
LABEL      version="3" \
           description="Sonatype Nexus 3+"

ENV NEXUS_LIB_PREFIX     /var/lib/nexus
ENV NEXUS_DATA_DIR       ${NEXUS_LIB_PREFIX}/data
ENV NEXUS_ETC_DIR        /etc/nexus
ENV NEXUS_TMP_DIR        /var/tmp/nexus

# BEGIN Configurable env vars

# ENV NEXUS_UID ...
ENV JAVA_MAX_HEAP        512m
ENV JAVA_MIN_HEAP        128m
ENV JAVA_VERSION_MAJOR   8
ENV JAVA_VERSION_MINOR   74
ENV JAVA_VERSION_BUILD   02

#END Configurable env vars

ENV NEXUS_PREFIX         /usr/local/share/nexus
ENV NEXUS_USER           nexus
ENV NEXUS_HOME           ${NEXUS_PREFIX}/default
ENV NEXUS_CERTS_DIR      ${NEXUS_ETC_DIR}/certificates
ENV NEXUS_DATA_CERTS_DIR ${NEXUS_DATA_DIR}/${NEXUS_CERTS_NAME}
ENV NEXUS_DISTRIBUTION   3
ENV NEXUS_VERSION        3.0.0-m7
ENV NEXUS_BUNDLE         unix
ENV NEXUS_EXTRACTED_DIR  nexus-3.0.0-b2016011501
ENV NEXUS_DOWNLOAD_URL   https://download.sonatype.com/nexus/${NEXUS_DISTRIBUTION}/nexus-${NEXUS_VERSION}-${NEXUS_BUNDLE}.tar.gz

ENV JAVA_PREFIX          /usr/local/share/java
ENV JAVA_HOME            ${JAVA_PREFIX}/default
ENV JAVA_SYSTEM          linux
ENV JAVA_ARCH            x64
ENV JAVA_DOWNLOAD_URL    http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/server-jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-${JAVA_SYSTEM}-${JAVA_ARCH}.tar.gz

RUN yum install -y \
  curl tar createrepo \
  && yum clean all

RUN echo "Installing Java from ${JAVA_DOWNLOAD_URL}" \
  && mkdir -p ${JAVA_PREFIX} \
  && curl --fail --silent --location --retry 3 \
    --header "Cookie: oraclelicense=accept-securebackup-cookie;" ${JAVA_DOWNLOAD_URL} \
  | gunzip \
  | tar -x -C ${JAVA_PREFIX} \
  && ln -s ${JAVA_PREFIX}/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}

RUN mkdir -p ${NEXUS_PREFIX} \
  && curl --fail --silent --location --retry 3 ${NEXUS_DOWNLOAD_URL} \
  | gunzip \
  | tar -x -C ${NEXUS_PREFIX} \
  && ln -s ${NEXUS_PREFIX}/${NEXUS_EXTRACTED_DIR} ${NEXUS_HOME}

RUN mkdir -p ${NEXUS_DATA_DIR} \
  && useradd -r -c "Sonatype Nexus user" -d ${NEXUS_DATA_DIR} -s /bin/bash ${NEXUS_USER} \
  && chown -R ${NEXUS_USER}:${NEXUS_USER} ${NEXUS_LIB_PREFIX} \
  && mkdir -p ${NEXUS_ETC_DIR} && cp -a ${NEXUS_HOME}/etc/. ${NEXUS_ETC_DIR} \
  && chown -R ${NEXUS_USER}:root ${NEXUS_ETC_DIR} && chmod 0700 ${NEXUS_ETC_DIR} \
  && mkdir -p ${NEXUS_TMP_DIR} && chown -R ${NEXUS_USER}:${NEXUS_USER} ${NEXUS_TMP_DIR}

RUN mkdir -p /usr/lib/systemd/system/
COPY nexus-env /usr/local/bin/
COPY nexus.service /usr/lib/systemd/system/

VOLUME ${NEXUS_DATA_DIR}
VOLUME ${NEXUS_ETC_DIR}

EXPOSE 8081
WORKDIR ${NEXUS_LIB_PREFIX}
ENTRYPOINT ["nexus-env"]
# ENTRYPOINT, CMD, variable expansion, execv, signal passing... Why all this inconsistency?

