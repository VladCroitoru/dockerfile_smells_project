FROM java:8-jdk

# VERSIONS
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.5}
ENV JENKINS_SHA ${JENKINS_SHA:-5e669825a955c9091ac8a858f4f6dcae782f3d87}
ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000
ENV RANCHER_COMPOSE v0.8.1
ENV DOCKER_COMPOSE 1.7.1

ENV PACKAGES apparmor docker-engine git curl zip

RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install -y apt-transport-https ca-certificates && \
    apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo deb https://apt.dockerproject.org/repo ubuntu-trusty main > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y $PACKAGES && \
    curl -s -L https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE/docker-compose-Linux-x86_64 > /usr/local/bin/docker-compose && \
    curl -s -L https://github.com/rancher/rancher-compose/releases/download/$RANCHER_COMPOSE/rancher-compose-linux-amd64-$RANCHER_COMPOSE.tar.gz -o rancher-compose.tar.gz && \
    tar -zxvf rancher-compose.tar.gz -C /usr/local/bin/ && \
    rm rancher-compose.tar.gz && \
    chmod -R +x /usr/local/bin && \
    rm -rf /var/lib/apt/lists/*

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} && \
    useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
VOLUME /var/jenkins_home

# `/usr/share/jenkins/ref/` contains all reference configuration we want
# to set on a fresh new installation. Use it to bundle additional plugins
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888

# Use tini as subreaper in Docker container to adopt zombie processes
RUN curl -fsSL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini \
  && echo "$TINI_SHA  /bin/tini" | sha1sum -c -

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy
COPY plugins.txt /usr/share/jenkins/plugins.txt

ARG JENKINS_VERSION
ARG JENKINS_SHA

# could use ADD but this one does not check Last-Modified header
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war && \
    echo "$JENKINS_SHA  /usr/share/jenkins/jenkins.war" | sha1sum -c -
    # from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh

ENV JENKINS_UC https://updates.jenkins.io
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref && \
    usermod -a -G docker jenkins && \
    /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

USER ${user}

COPY jenkins.sh /usr/local/bin/jenkins.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
