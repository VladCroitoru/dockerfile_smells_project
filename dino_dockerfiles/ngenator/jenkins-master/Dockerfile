FROM jenkins:alpine

MAINTAINER Daniel Ng <ngenator@gmail.com>

ENV JENKINS_USER=${JENKINS_USER:-jenkins}
ENV JENKINS_PASS=${JENKINS_PASS:-jenkins}
ENV EXECUTORS=${EXECUTORS:-0}

# Install initial required plugins
ENV SWARM_CLIENT_VERSION 3.3
RUN /usr/local/bin/install-plugins.sh \
    swarm:${SWARM_CLIENT_VERSION}

ONBUILD COPY ./plugins.txt /usr/share/jenkins/ref/plugins.txt

ONBUILD RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

# Add the groovy scripts that configure jenkins
COPY init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/

# Don't prompt for user to install additional plugins
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

COPY log.properties ${JENKINS_HOME}

HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:8080/ || exit 1
