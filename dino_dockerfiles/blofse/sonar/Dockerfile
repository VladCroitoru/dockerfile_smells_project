FROM openjdk:8-alpine

ENV SONAR_VERSION=7.3 \
    SONARQUBE_HOME=/opt/sonarqube \
    # Database configuration
    # Defaults to using H2
    SONARQUBE_JDBC_USERNAME=sonar \
    SONARQUBE_JDBC_PASSWORD=sonar \
    SONARQUBE_JDBC_URL= \
    SONAR_DOWNLOAD_URL=https://binaries.sonarsource.com/Distribution \
    SONAR_JAVA_PLUGIN_VERSION=5.8.0.15699 \
    SONAR_HTML_PLUGIN=3.0.1.1444

COPY run.sh ${SONARQUBE_HOME}/bin/

RUN set -x \
    && apk add --no-cache gnupg unzip libressl wget tzdata bash \
    && (gpg --keyserver ha.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE \
      || gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE) \
    && wget -O sonarqube.zip --no-verbose "${SONAR_DOWNLOAD_URL}/sonarqube/sonarqube-${SONAR_VERSION}.zip" \
    && wget -O sonarqube.zip.asc --no-verbose "${SONAR_DOWNLOAD_URL}/sonarqube/sonarqube-${SONAR_VERSION}.zip.asc" \ 
    && gpg --batch --verify sonarqube.zip.asc sonarqube.zip \
    && unzip sonarqube.zip \
    && mkdir -p "${SONARQUBE_HOME}" \
    && cp -R sonarqube-${SONAR_VERSION}/* "${SONARQUBE_HOME}/" \
    && rm sonarqube.zip \
    && rm -rf /sonarqube-${SONAR_VERSION}/*.* \
    && mkdir -p "${SONARQUBE_HOME}/extensions/plugins/" \
    && cd "${SONARQUBE_HOME}/extensions/plugins/" \
    && wget -O sonar-java-plugin-${SONAR_JAVA_PLUGIN_VERSION}.jar --no-verbose "${SONAR_DOWNLOAD_URL}/sonar-java-plugin/sonar-java-plugin-${SONAR_JAVA_PLUGIN_VERSION}.jar" \
    && wget -O sonar-html-plugin-${SONAR_HTML_PLUGIN}.jar --no-verbose "${SONAR_DOWNLOAD_URL}/sonar-html-plugin/sonar-html-plugin-${SONAR_HTML_PLUGIN}.jar" \
    && adduser -D -u 1000 sonar \
    && chown -R sonar "${SONARQUBE_HOME}" \
    && chmod -R 755 "${SONARQUBE_HOME}" \
    && chown sonar "${SONARQUBE_HOME}/bin/run.sh" \
    && chmod +x "${SONARQUBE_HOME}/bin/run.sh"

EXPOSE 9000

VOLUME ["${SONARQUBE_HOME}/data", "${SONARQUBE_HOME}/extensions", "${SONARQUBE_HOME}/conf", "${SONARQUBE_HOME}/temp"]

# Setup the working dir and run file
WORKDIR ${SONARQUBE_HOME}

USER sonar
ENTRYPOINT ["./bin/run.sh"]

