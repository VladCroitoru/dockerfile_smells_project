
FROM alpine:3

EXPOSE 8080 22222

ARG BUILD_DATE
ARG BUILD_VERSION
ARG TOMCAT_VERSION
ARG JOLOKIA_VERSION
ARG HAWTIO_VERSION

ENV \
  TERM=xterm \
  CATALINA_HOME=/opt/tomcat \
  JAVA_HOME=/usr/lib/jvm/default-jvm \
  PATH=${PATH}:/opt/jdk/bin:${CATALINA_HOME}/bin

# ---------------------------------------------------------------------------------------------------------------------

# hadolint ignore=SC2035,DL3003,DL3017,DL3018,DL4006
RUN \
  apk update  --quiet --no-cache && \
  apk upgrade --quiet --no-cache && \
  apk add     --quiet --no-cache \
    curl \
    nss \
    openjdk11-jre-headless \
    tomcat-native && \
  echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
  echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
  sed -i 's,#networkaddress.cache.ttl=-1,networkaddress.cache.ttl=30,' "${JAVA_HOME}/jre/conf/security/java.security" && \
  [ -d /opt ] || mkdir /opt 2> /dev/null && \
  echo "download tomcat version $TOMCAT_VERSION (https://archive.apache.org/dist/tomcat/tomcat-9/)" && \
  curl \
    --silent \
    --location \
    --retry 3 \
    --cacert /etc/ssl/certs/ca-certificates.crt \
    "https://archive.apache.org/dist/tomcat/tomcat-9/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz" \
    | gunzip \
    | tar x -C /opt/ && \
  ln -s "/opt/apache-tomcat-$TOMCAT_VERSION" "${CATALINA_HOME}" && \
  ln -s "${CATALINA_HOME}/logs" /var/log/jolokia && \
  rm -rf "${CATALINA_HOME}/webapps/*" && \
  echo "download jolokia version $JOLOKIA_VERSION (https://repo1.maven.org/maven2/org/jolokia/jolokia-war)" && \
  curl \
    --silent \
    --location \
    --retry 3 \
    --cacert /etc/ssl/certs/ca-certificates.crt \
    --output "${CATALINA_HOME}/webapps/jolokia.war" \
    "https://repo1.maven.org/maven2/org/jolokia/jolokia-war/$JOLOKIA_VERSION/jolokia-war-$JOLOKIA_VERSION.war" && \
  echo "download hawtio version $HAWTIO_VERSION (https://github.com/hawtio/hawtio/tags)" && \
  curl \
    --silent \
    --location \
    --retry 3 \
    --cacert /etc/ssl/certs/ca-certificates.crt \
    --output "${CATALINA_HOME}/webapps/hawtio.war" \
    "https://oss.sonatype.org/content/repositories/public/io/hawt/hawtio-default/$HAWTIO_VERSION/hawtio-default-$HAWTIO_VERSION.war" && \
  cd "${CATALINA_HOME}/webapps/" && \
  mkdir \
    jolokia hawtio && \
  unzip jolokia.war -d jolokia > /dev/null && \
  unzip hawtio.war  -d hawtio  > /dev/null && \
  rm -f *.war && \
  rm -f "${CATALINA_HOME}/LICENSE" && \
  rm -f "${CATALINA_HOME}/NOTICE" && \
  rm -f "${CATALINA_HOME}/RELEASE-NOTES" && \
  rm -f "${CATALINA_HOME}/RUNNING.txt" && \
  rm -f "${CATALINA_HOME}/bin/*.bat" && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

WORKDIR ${CATALINA_HOME}/webapps/

COPY rootfs/ /

CMD ["/init/run.sh"]

HEALTHCHECK \
  --interval=5s \
  --timeout=2s \
  --retries=12 \
  CMD /init/healthcheck.sh

# ---------------------------------------------------------------------------------------------------------------------

LABEL \
  version=${BUILD_VERSION} \
  maintainer="Bodo Schulz <bodo@boone-schulz.de>" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Jolokia Docker Image" \
  org.label-schema.description="Inofficial Jolokia Docker Image" \
  org.label-schema.url="https://jolokia.org" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-jolokia" \
  org.label-schema.vcs-ref=${VCS_REF} \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${JOLOKIA_VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="GNU General Public License v3.0"

# ---------------------------------------------------------------------------------------------------------------------
