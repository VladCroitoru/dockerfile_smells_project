FROM openjdk:8-jdk

MAINTAINER Adrien Missemer <adrien.missemer@gmail.com>

ENV JENKINS_SWARM_VERSION 2.2
ENV JENKINS_SLAVE_HOME /var/lib/jenkins_slave
ENV TINI_VERSION v0.9.0

#
# Docker install
#

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo deb https://apt.dockerproject.org/repo debian-jessie main > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-engine \
    && rm -rf /var/lib/apt/lists/*

#
# Swarm install
# 

RUN curl --create-dirs -sSLo \
    /usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar \
    http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar && \
    chmod 755 /usr/share/jenkins

# grab tini for signal processing and zombie killing
RUN set -x \
    && curl -fSL "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini" -o /usr/local/bin/tini \
    && curl -fSL "https://github.com/krallin/tini/releases/download/$TINI_VERSION/tini.asc" -o /usr/local/bin/tini.asc \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 6380DC428747F6C393FEACA59A84159D7001A4E5 \
    && gpg --batch --verify /usr/local/bin/tini.asc /usr/local/bin/tini \
    && rm -r "$GNUPGHOME" /usr/local/bin/tini.asc \
    && chmod +x /usr/local/bin/tini \
    && tini -h
#

VOLUME $JENKINS_SLAVE_HOME

COPY jenkins-slave-entrypoint.sh /usr/local/bin/
# Use tini as subreaper in Docker container to adopt zombie processes 
ENTRYPOINT ["tini", "--", "jenkins-slave-entrypoint.sh"]
