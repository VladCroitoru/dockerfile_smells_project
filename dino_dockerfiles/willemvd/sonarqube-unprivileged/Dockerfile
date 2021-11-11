FROM sonarqube:6.4-alpine
MAINTAINER willemvd <willemvd@github>

# Database configuration
# Defaults to using H2, can be overriden with environment variables:
#SONARQUBE_JDBC_USERNAME=sonar
#SONARQUBE_JDBC_PASSWORD=sonar
#SONARQUBE_JDBC_URL=

VOLUME ["${SONARQUBE_HOME}/data", "${SONARQUBE_HOME}/extensions"]

RUN adduser -u 99 -S -G root -H sonarqube && \
    chmod -R g+w ${SONARQUBE_HOME}

USER sonarqube

ENTRYPOINT ["./bin/run.sh"]
