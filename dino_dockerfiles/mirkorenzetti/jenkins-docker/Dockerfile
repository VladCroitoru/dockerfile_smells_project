FROM jenkins/jenkins:latest

USER root

RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common

RUN curl -fsSL get.docker.com -o get-docker.sh
RUN sh get-docker.sh

RUN usermod -aG docker jenkins
USER jenkins
