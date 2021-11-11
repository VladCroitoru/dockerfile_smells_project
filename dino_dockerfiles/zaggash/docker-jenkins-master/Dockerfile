FROM jenkins/jenkins:lts-alpine

USER root

RUN \
  apk add --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/v3.6/community \
    docker

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN \
  /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt && \
  echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

USER jenkins
