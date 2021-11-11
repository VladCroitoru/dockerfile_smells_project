# FROM eryk81/jenkins-agent-arm64
FROM debian:buster
LABEL arch="arm|arm64"

ARG remotingversion=4.10
ARG k3sversion=1.22.2%2Bk3s1

ARG jenkinsagent=https://repo.jenkins-ci.org/releases/org/jenkins-ci/main/remoting/$remotingversion/remoting-$remotingversion.jar
ARG dockerrepo=https://download.docker.com/linux/debian

# ADD https://raw.githubusercontent.com/jenkinsci/docker-inbound-agent/master/jenkins-agent /default-entrypoint.sh
COPY default-entrypoint.sh /default-entrypoint.sh
RUN chmod +x /default-entrypoint.sh

ADD $jenkinsagent /usr/share/jenkins/agent.jar

RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
      wget curl software-properties-common gnupg2 \
      git \
      openjdk-11-jdk-headless maven \
      npm nodejs \
      && \

    curl -fsSL --insecure $dockerrepo/gpg | apt-key add - && \

    REL=$(lsb_release -cs) && \
    add-apt-repository "deb $dockerrepo $REL stable" && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends --no-install-suggests \
      docker-ce docker-ce-cli containerd.io && \

    rm -rf /var/lib/apt/lists/* && \

    wget -O k3s https://github.com/k3s-io/k3s/releases/download/v$k3sversion/k3s-armhf && \
    mv ./k3s /usr/local/bin/k3s && \
    chmod +x /usr/local/bin/k3s && \

    echo 'Done'

VOLUME /root/.m2
VOLUME /root/.kube
VOLUME /root/.docker
VOLUME /etc/docker/daemon.json

ENTRYPOINT [ "/bin/sh", "-c", "/default-entrypoint.sh" ]