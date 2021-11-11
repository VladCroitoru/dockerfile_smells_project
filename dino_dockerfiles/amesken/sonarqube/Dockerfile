FROM sonarqube:5.2

MAINTAINER Andries Mesken <andries.mesken@ziggo.nl>

ENV SONAR_DOWNLOAD_URL https://sonarsource.bintray.com/Distribution
ENV SONARQUBE_HOME /opt/sonarqube

# Installing Plugins
RUN cd /opt/sonarqube/extensions/plugins/ \
  && curl -o sonar-java-plugin-3.5.jar -fSL $SONAR_DOWNLOAD_URL/sonar-java-plugin/sonar-java-plugin-3.5.jar \
  && curl -o sonar-web-plugin-2.4.jar -fSL $SONAR_DOWNLOAD_URL/sonar-web-plugin/sonar-web-plugin-2.4.jar \
  && curl -o sonar-scm-git-plugin-1.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-scm-git-plugin/1.1/sonar-scm-git-plugin-1.1.jar

RUN mkdir -p /c/Users/Andries/docker/data/sonarqube/data && chmod 777 /c/Users/Andries/docker/data/sonarqube/data && \ 
  mkdir -p /c/Users/Andries/docker/data/sonarqube/logs && chmod 777 /c/Users/Andries/docker/data/sonarqube/logs && \ 
  mkdir -p /c/Users/Andries/docker/data/sonarqube/extensions && chmod 777 /c/Users/Andries/docker/data/sonarqube/extensions

VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/logs", "$SONARQUBE_HOME/extensions"]

WORKDIR $SONARQUBE_HOME
COPY run.sh $SONARQUBE_HOME/bin/
RUN chmod +x $SONARQUBE_HOME/bin/run.sh

ENTRYPOINT ["./bin/run.sh"]
