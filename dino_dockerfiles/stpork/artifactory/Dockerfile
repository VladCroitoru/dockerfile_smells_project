FROM openjdk:8-jdk

MAINTAINER stpork from Mordor team

ENV ARTIFACTORY_VERSION=5.8.1 \
ARTIFACTORY_HOME=/var/opt/artifactory \
ARTIFACTORY_DATA=/data/artifactory \
ARTIFACTORY_URL=http://artifactory:8081/artifactory \
HAZELCAST_INTERFACE=10.*.*.* \
HAZELCAST_PORT=10001 \
DB_HOST=postgresql \
DB_PORT=5432 \
DB_USER=artifactory \
DB_NAME=artifactory \
DB_PASSWORD=JEurqTbgSUbf7QbTndZ8Ckb1ZyRAociRRGqFHYhzwAuio9bu1LQtniqnQkSNXHsH7i1tGS6

ENV TOMCAT_HOME=${ARTIFACTORY_HOME}/tomcat

RUN set -x \
&& mkdir -p /var/opt  \
&& cd /var/opt \
&& ARTIFACTORY_INSTALL=artifactory-pro-${ARTIFACTORY_VERSION} \
&& PACKAGE=jfrog-${ARTIFACTORY_INSTALL}.zip \
&& curl -fsSL \
"https://bintray.com/jfrog/artifactory-pro/download_file?file_path=org/artifactory/pro/jfrog-artifactory-pro/${ARTIFACTORY_VERSION}/${PACKAGE}" \
-o ${PACKAGE} \
&& unzip -q ${PACKAGE} \
&& mv ${ARTIFACTORY_INSTALL}/etc ${ARTIFACTORY_INSTALL}/etc-clean \
&& rm -rf ${PACKAGE} ${ARTIFACTORY_INSTALL}/logs \
&& mv ${ARTIFACTORY_INSTALL} ${ARTIFACTORY_HOME} \
&& find $ARTIFACTORY_HOME -type f -name "*.exe" -o -name "*.bat" | xargs /bin/rm \
&& mkdir -p ${ARTIFACTORY_DATA} \
&& ln -s ${ARTIFACTORY_DATA}/access ${ARTIFACTORY_HOME}/access \
&& ln -s ${ARTIFACTORY_DATA}/backup ${ARTIFACTORY_HOME}/backup \
&& ln -s ${ARTIFACTORY_DATA}/data ${ARTIFACTORY_HOME}/data \
&& ln -s ${ARTIFACTORY_DATA}/logs ${ARTIFACTORY_HOME}/logs \
&& ln -s ${ARTIFACTORY_DATA}/run ${ARTIFACTORY_HOME}/run \
&& ln -s ${ARTIFACTORY_DATA}/etc ${ARTIFACTORY_HOME}/etc \
&& sed -i 's/-n "\$ARTIFACTORY_PID"/-d $(dirname "$ARTIFACTORY_PID")/' $ARTIFACTORY_HOME/bin/artifactory.sh \
&& echo 'if [ ! -z "${EXTRA_JAVA_OPTIONS}" ]; then export JAVA_OPTIONS="$JAVA_OPTIONS $EXTRA_JAVA_OPTIONS"; fi' >> $ARTIFACTORY_HOME/bin/artifactory.default \
&& POSTGRESQL_JAR=postgresql-42.1.4.jar \
&& curl -fsSL \
"https://jdbc.postgresql.org/download/${POSTGRESQL_JAR}" \
-o $TOMCAT_HOME/lib/${POSTGRESQL_JAR} \
&& chown -R 1001:0 ${ARTIFACTORY_HOME} \
&& chmod -R 777 ${ARTIFACTORY_HOME} \
&& chown -R 1001:0 ${ARTIFACTORY_DATA} \
&& chmod -R 777 ${ARTIFACTORY_DATA}

COPY entrypoint.sh /entrypoint.sh

# Drop privileges
RUN chown -R 1001:0 /entrypoint.sh \
&& chmod -R 755 /entrypoint.sh

USER 1001

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8081/artifactory || exit 1

# Expose Artifactories data directory
VOLUME ["${ARTIFACTORY_DATA}"]

WORKDIR ${ARTIFACTORY_DATA}

EXPOSE 8081 8019

ENTRYPOINT ["/entrypoint.sh"]
