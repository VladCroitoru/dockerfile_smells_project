FROM ubuntu:14.04

MAINTAINER Jonathan Parrilla <Jonathan.Parrilla@outlook.com>

# Install the basics
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables

# Install Docker
RUN curl -sSL https://get.docker.com/ | sh

# Add the wrapper script. Obtained from https://raw.githubusercontent.com/docker/docker/master/hack/dind.
ADD ./dind /usr/local/bin/dind
RUN chmod +x /usr/local/bin/dind

ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Define a volume for our image.
VOLUME /var/lib/docker

ENV DOCKER_COMPOSE_VERSION 1.3.3

# Install Jenkins
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-get update && apt-get install -y zip supervisor jenkins && rm -rf /var/lib/apt/lists/*
RUN usermod -a -G docker jenkins
ENV JENKINS_HOME /var/lib/jenkins
VOLUME /var/lib/jenkins

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs

# Install Cross Browser Testing Tunnels
RUN npm install -g cbt_tunnels

# Install Dependecies
npm install lodash --save
npm install request -g
npm install clui -g
npm install cli-color -g
npm install yargs -g
npm install socket.io-client -g

# Add supervisord
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 8080
EXPOSE 8080

# Run supervisord via CMD
CMD ["/usr/bin/supervisord"]
