FROM jenkins/jenkins:2.138-alpine

MAINTAINER ragetti 

ENV JENKINS_USER=jenkins
USER root
RUN apk --no-cache add shadow su-exec
RUN curl https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz | tar xvz -C /tmp/ && mv /tmp/docker/docker /usr/bin/docker

COPY entrypoint.sh /usr/local/bin/

CMD ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]

