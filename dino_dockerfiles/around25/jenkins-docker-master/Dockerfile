FROM ubuntu:16.04
MAINTAINER Cosmin Harangus <cosmin@around25.com>

EXPOSE 8080
ENV DOCKER_COMPOSE_VERSION 1.13.0
ENV JENKINS_HOME /var/lib/jenkins

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables

# Install Docker
RUN curl -sSL https://get.docker.com/ | sh

# Install Jenkins
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-get update && apt-get install -y zip jenkins && rm -rf /var/lib/apt/lists/*
RUN usermod -a -G docker jenkins
VOLUME /var/lib/jenkins

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

CMD ["/usr/bin/java",  "-jar",  "/usr/share/jenkins/jenkins.war"]
