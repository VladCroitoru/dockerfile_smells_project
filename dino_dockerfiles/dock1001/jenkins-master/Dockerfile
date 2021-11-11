FROM jenkins/jenkins:latest

# Install the docker CLI
# https://getintodevops.com/blog/the-simple-way-to-run-docker-in-docker-for-ci
# Also Inspired by https://github.com/Shimmi/docker-jenkins

USER root

RUN apt-get update \
 && apt-get -y install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common \
 && rm -rf /var/lib/apt/lists/*

# Add docker client
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey \
 && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable" \
 && apt-get update \
 && apt-get -q -y install docker-ce \
 && rm -rf /var/lib/apt/lists/*

# Prepare jenkins
USER jenkins

# Set the number of executors
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

# Install Jenkins plugins
RUN install-plugins.sh \
    blueocean \
    cloudbees-bitbucket-branch-source \
    dockerhub-notification \
    docker-workflow \
    gerrit-trigger \
    git \
    locale \
    pipeline-stage-view \
    swarm \
    workflow-aggregator
