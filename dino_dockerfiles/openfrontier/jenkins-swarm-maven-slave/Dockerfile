FROM openfrontier/jenkins-swarm-slave

MAINTAINER zsx <thinkernel@gmail.com>

ENV MAVEN_VERSION 3.5.4
ENV MAVEN_HOME /usr/share/maven

USER root
RUN curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
   | tar -xzC /usr/share \
  && mv "/usr/share/apache-maven-${MAVEN_VERSION}" "${MAVEN_HOME}" \
  && ln -s "${MAVEN_HOME}/bin/mvn" /usr/bin/mvn
USER "${JENKINS_USER}"

ENV MAVEN_CONFIG ${JENKINS_HOME}/.m2
