FROM debian:jessie-backports

MAINTAINER Marcelo Almeida <ms.almeida86@gmail.com>

ENV DEBIAN_FRONTEND "noninteractive"

# Let's start with some basic stuff.
RUN apt-get update && apt-get -t jessie-backports install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables \
    git \
    zip \
    supervisor \
    openjdk-8-jdk-headless \
    ca-certificates-java && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Install the wrapper script from https://raw.githubusercontent.com/docker/docker/master/hack/dind.
ADD https://raw.githubusercontent.com/docker/docker/master/hack/dind /usr/local/bin/dind
RUN chmod +x /usr/local/bin/dind

ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define additional metadata for our image.
VOLUME /var/lib/docker

ENV \
  JENKINS_HOME="/var/lib/jenkins/"
RUN \
  mkdir ${JENKINS_HOME} && \
  useradd jenkins --home-dir ${JENKINS_HOME} && \
  chown jenkins:jenkins ${JENKINS_HOME} && \
  usermod -a -G docker jenkins

# Download Jenkins Swarm plugin
ENV SWARM_VERSION 3.4
ADD https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_VERSION}/swarm-client-${SWARM_VERSION}.jar /root/swarm-client.jar

ENV \
  URL="" \
  USERNAME="" \
  PASSWORD="" \
  FSROOT="${JENKINS_HOME}" \
  EXECUTORS="1" \
  GIT_TIMEOUT="60" \
  MAX_HEAP_SIZE="512m" \
  MAX_PERM_SIZE="2048m"

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
