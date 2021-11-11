#
# All credits to this project: https://github.com/jenkinsci/docker-jnlp-slave
#

FROM openjdk:8-jdk
MAINTAINER Lorenzo Arribas <lorenzo.arribas@me.com>

RUN apt-get update
RUN apt-get install -y openssh-server

ENV HOME /home/jenkins
RUN groupadd -g 10000 jenkins
RUN useradd -c "Jenkins user" -d $HOME -u 10000 -g 10000 -m jenkins

ARG VERSION=2.62
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

USER jenkins
RUN mkdir /home/jenkins/.jenkins
VOLUME /home/jenkins/.jenkins
WORKDIR /home/jenkins

COPY jenkins-slave /usr/local/bin/jenkins-slave
ENTRYPOINT ["jenkins-slave"]
