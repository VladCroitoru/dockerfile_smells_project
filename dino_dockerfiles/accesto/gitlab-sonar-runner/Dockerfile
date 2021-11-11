FROM java:openjdk-8u45-jre
MAINTAINER Michal Kurzeja accesto.com

ENV SONAR_RUNNER_VERSION 2.4
ENV SONAR_RUNNER_HOME /opt/sonar-runner-${SONAR_RUNNER_VERSION}
ENV SONAR_RUNNER_PACKAGE sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip
ENV HOME ${SONAR_RUNNER_HOME}

WORKDIR /opt

RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/${SONAR_RUNNER_VERSION}/${SONAR_RUNNER_PACKAGE} \
 && unzip sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip \
 && rm ${SONAR_RUNNER_PACKAGE}

RUN groupadd -r sonar \
 && useradd -r -s /usr/sbin/nologin -d ${SONAR_RUNNER_HOME} -c "Sonar service user" -g sonar sonar \
 && chown -R sonar:sonar ${SONAR_RUNNER_HOME} \
 && mkdir -p /data \
 && chown -R sonar:sonar /data

WORKDIR /data
VOLUME /data
USER sonar

COPY gitlab-entrypoint.sh /gitlab-entrypoint.sh
ENTRYPOINT ["/gitlab-entrypoint.sh"]
CMD ${SONAR_RUNNER_HOME}/bin/sonar-runner
