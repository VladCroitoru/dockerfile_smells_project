FROM openjdk:8-jre-stretch

MAINTAINER Bertrand Roussel <broussel@sierrawireless.com>

# Release
ENV JENKINS_SWARM_VERSION 3.13
ENV SWARM_PLUGIN_URL https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar

# Snapshot
#ENV JENKINS_BUILD lastStableBuild
#ENV JENKINS_SWARM_VERSION 3.6-SNAPSHOT
#ENV SWARM_PLUGIN_URL https://jenkins.ci.cloudbees.com/job/plugins/job/swarm-plugin/$JENKINS_BUILD/org.jenkins-ci.plugins\$swarm-client/artifact/org.jenkins-ci.plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION.jar

# Dev build
#ENV SWARM_PLUGIN_URL https://github.com/CoRfr/swarm-plugin/releases/download/swarm-plugin-$JENKINS_SWARM_VERSION/swarm-client-jar-with-dependencies.jar

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG JENKINS_AGENT_HOME=/home/${user}

COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh
COPY install.sh /tmp/install.sh

RUN /tmp/install.sh

VOLUME /opt/tini
ENTRYPOINT ["/opt/tini/tini", "--", "/usr/local/bin/jenkins-slave.sh"]

USER ${user}
VOLUME ${JENKINS_AGENT_HOME}

