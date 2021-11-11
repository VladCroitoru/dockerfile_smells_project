FROM jenkins/jenkins:2.145-alpine

USER root
RUN apk update && \
    apk add bash git openssh rsync procps && \
    rm -rf /var/cache/apk/*

USER jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt | tr '\n' ' ')

ENV CASC_JENKINS_CONFIG=/var/jenkins_home/zebra/casc
