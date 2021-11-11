FROM openjdk:8-jdk
MAINTAINER Steve Wade <steven@stevenwade.co.uk> (@swade1987)

# Set necessary environment variables
ENV JENKINS_VERSION=1.651.3
ENV TINI_VERSION 0.9.0
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000
ENV JENKINS_UC https://updates.jenkins.io
ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

RUN apt-get update && apt-get install -y git curl && \
    mkdir -p /usr/share/jenkins && \
    curl -fsSL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war && \
    mkdir -p ${JENKINS_HOME}/plugins

ADD plugins/ $JENKINS_HOME/plugins/

RUN chown -R root:root "$JENKINS_HOME"

USER root
VOLUME /var/jenkins_home
EXPOSE 8080 50000
CMD ["java","-jar","/usr/share/jenkins/jenkins.war"]