# Artifactory for OpenShift
#
# VERSION 		5.4.1epos

FROM openjdk:8-jdk

# loosely based on existing repository https://github.com/fkirill/dockerfile-artifactory
MAINTAINER Daniel Zauner <daniel.zauner@epos-cat.de>

ENV \
  ARTIFACTORY_HOME=/var/opt/artifactory \
  ARTIFACTORY_DATA=/data/artifactory \
  ARTIFACTORY_USER_ID=1030 \
  DB_HOST=postgresql \
  DB_PORT=5432 \
  DB_USER=artifactory \
  DB_PASSWORD=password \
  DB_NAME=artifactory


# Fetch and install Artifactory Pro
# =================================
# For the latest version and checksum, check https://bintray.com/jfrog/artifactory-pro/jfrog-artifactory-pro-zip/_latestVersion
#
# - Define version and SHA256 checksum
# - Fetch the zipfile from bintray
# - Validate the archvie
# - Extract and move to the correct folder
# - Remove Windows executables
# - Remove temporary files
# - Link folders (etc folder is copied over and linked back to preserve stock config)
# - Fix a test in startup script to follow symlink
# - Add option to inject custom JAVA_OPTIONS via environment variable EXTRA_JAVA_OPTIONS
RUN \
  ARTIFACTORY_VERSION=5.4.4 \
  ARTIFACTORY_SHA256=f2f258afcd5692f4a3618ba6dc6808f2c997d5e764cc2679b14f53e2e7b38f91 \
  ARTIFACTORY_URL=https://bintray.com/jfrog/artifactory-pro/download_file?file_path=org/artifactory/pro/jfrog-artifactory-pro/${ARTIFACTORY_VERSION}/jfrog-artifactory-pro-${ARTIFACTORY_VERSION}.zip \
  ARTIFACTORY_TEMP=$(mktemp -t "$(basename $0).XXXXXXXXXX.zip") && \
  curl -L -o ${ARTIFACTORY_TEMP} ${ARTIFACTORY_URL} && \
  printf '%s\t%s\n' $ARTIFACTORY_SHA256 $ARTIFACTORY_TEMP | sha256sum -c && \
  unzip -q $ARTIFACTORY_TEMP -d /tmp && \
  mv /tmp/artifactory-pro-${ARTIFACTORY_VERSION} ${ARTIFACTORY_HOME} && \
  find $ARTIFACTORY_HOME -type f -name "*.exe" -o -name "*.bat" | xargs /bin/rm && \
  rm -r $ARTIFACTORY_TEMP ${ARTIFACTORY_HOME}/logs && \
  ln -s ${ARTIFACTORY_DATA}/access ${ARTIFACTORY_HOME}/access && \
  ln -s ${ARTIFACTORY_DATA}/backup ${ARTIFACTORY_HOME}/backup && \
  ln -s ${ARTIFACTORY_DATA}/data ${ARTIFACTORY_HOME}/data && \
  ln -s ${ARTIFACTORY_DATA}/logs ${ARTIFACTORY_HOME}/logs && \
  ln -s ${ARTIFACTORY_DATA}/run ${ARTIFACTORY_HOME}/run && \
  mv ${ARTIFACTORY_HOME}/etc ${ARTIFACTORY_HOME}/etc-clean && \
  ln -s ${ARTIFACTORY_DATA}/etc ${ARTIFACTORY_HOME}/etc && \
  sed -i 's/-n "\$ARTIFACTORY_PID"/-d $(dirname "$ARTIFACTORY_PID")/' $ARTIFACTORY_HOME/bin/artifactory.sh && \
  echo 'if [ ! -z "${EXTRA_JAVA_OPTIONS}" ]; then export JAVA_OPTIONS="$JAVA_OPTIONS $EXTRA_JAVA_OPTIONS"; fi' >> $ARTIFACTORY_HOME/bin/artifactory.default


# Setup PostgreSQL
# ================
#
# - Grab PostgreSQL driver
# - Copy PostgreSQL properties
# - Insert connection information (DB_USER, DB_PASSWORD, DB_HOST)
RUN \
  POSTGRESQL_JAR_VERSION=9.4.1212 \
  POSTGRESQL_JAR=https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_JAR_VERSION}.jar && \
  curl -L -o $ARTIFACTORY_HOME/tomcat/lib/postgresql-${POSTGRESQL_JAR_VERSION}.jar ${POSTGRESQL_JAR}

# Change default port to 8080
RUN sed -i 's/port="8081"/port="8080"/' ${ARTIFACTORY_HOME}/tomcat/conf/server.xml

# Install netstat for artifactoryctl to work properly
# FIXME: needed?
#RUN apt-get update && apt-get install -y net-tools

COPY files/entrypoint-artifactory.sh /

# Drop privileges
RUN \
  chown -R ${ARTIFACTORY_USER_ID}:${ARTIFACTORY_USER_ID} ${ARTIFACTORY_HOME} && \
  chmod -R 777 ${ARTIFACTORY_HOME} && \
  chown -R ${ARTIFACTORY_USER_ID}:${ARTIFACTORY_USER_ID} /entrypoint-artifactory.sh && \
  chmod -R 777 /entrypoint-artifactory.sh


USER $ARTIFACTORY_USER_ID

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8080/artifactory || exit 1

# Expose Artifactories data directory
VOLUME ["/data/artifactory", "/data/artifactory/backup"]

WORKDIR /data/artifactory

EXPOSE 8080

ENTRYPOINT ["/entrypoint-artifactory.sh"]
