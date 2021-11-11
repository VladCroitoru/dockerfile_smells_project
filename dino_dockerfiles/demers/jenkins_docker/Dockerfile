# Inspiré de https://tripdubroot.com/jenkins-docker-in-docker-dind-2040cc90eeab

# Version Jenkins LTS
FROM jenkins/jenkins:lts

# Installation via le compte root
USER root

# Mise à jour du système
RUN apt-get -y update

# Préalable pour installer Docker
RUN apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    gnupg2 \
    software-properties-common

# Docker repos
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
     $(lsb_release -cs) \
     stable"

RUN apt-get update

# Installation de Docker
RUN apt-get -y install docker-ce

# Installation docker-compose 1.27.4
RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Donner les droits d'utiliser Docker à Jenkins
RUN usermod -aG docker jenkins

RUN apt-get -y update && apt-get install -y locales && locale-gen fr_CA.UTF-8
ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

## Clean up when done
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



