FROM ubuntu:16.04
MAINTAINER Cosmin Harangus <cosmin@around25.com>

ENV DOCKER_COMPOSE_VERSION 1.13.0
ENV SWARM_CLIENT_VERSION 2.2

RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl

# Install Docker
RUN curl -sSL https://get.docker.com/ | sh

# Add a Jenkins user with permission to run docker commands
RUN useradd -r -m -G docker jenkins

# Install necessary packages
RUN apt-get update && apt-get install -y openjdk-8-jre-headless && rm -rf /var/lib/apt/lists/*

# Install Jenkins Swarm Client
RUN curl -L http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}-jar-with-dependencies.jar > /home/jenkins/swarm-client-${SWARM_CLIENT_VERSION}-jar-with-dependencies.jar

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

WORKDIR /home/jenkins

CMD /usr/bin/java -jar swarm-client-${SWARM_CLIENT_VERSION}-jar-with-dependencies.jar $COMMAND_OPTIONS
