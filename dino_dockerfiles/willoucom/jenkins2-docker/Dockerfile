FROM jenkinsci/jenkins:latest
USER root

RUN \
    apt-get purge lxc-docker* | true \
    && apt-get purge docker.io* | true \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo "deb http://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y docker-engine \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
