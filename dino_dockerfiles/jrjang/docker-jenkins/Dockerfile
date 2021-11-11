FROM debian:latest
MAINTAINER jrjang@gmail.com

USER root

ENV TZ="Asia/Taipei"

RUN apt-get update \
 && apt-get install -y wget python-pip python-dev sudo

RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add - \
 && echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list

RUN apt-get update \
 && apt-get install -y jenkins

COPY jenkins /etc/sudoers.d/jenkins
COPY pip_install.sh /usr/local/bin/pip_install.sh
copy run.sh /usr/local/bin/run.sh

USER jenkins

ENTRYPOINT ["/usr/local/bin/run.sh"]
