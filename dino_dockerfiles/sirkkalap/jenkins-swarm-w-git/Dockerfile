FROM csanchez/jenkins-swarm

MAINTAINER Petri Sirkkala <sirpete@iki.fi>

# I like utf-8 (mostly)
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8

# Time zone
RUN echo "Europe/Helsinki" > /etc/timezone \
 && dpkg-reconfigure --frontend=noninteractive tzdata

ENV GIT_HOME /usr/bin/git

ENV JENKINS_SSH_CREDENTIALS_VERSION 1.10

RUN curl -sSL --create-dirs -o /usr/share/jenkins/plugins/ssh-credentials.hpi https://updates.jenkins-ci.org/download/plugins/ssh-credentials/$JENKINS_SSH_CREDENTIALS_VERSION/ssh-credentials.hpi

ENV JENKINS_CREDENTIALS_VERSION 1.20

RUN curl -sSL --create-dirs -o /usr/share/jenkins/plugins/credentials.hpi https://updates.jenkins-ci.org/download/plugins/credentials/$JENKINS_CREDENTIALS_VERSION/credentials.hpi

ENV JENKINS_GIT_CLIENT_VERSION 1.14.0

RUN curl -sSL --create-dirs -o /usr/share/jenkins/plugins/git-client.hpi https://updates.jenkins-ci.org/download/plugins/git-client/$JENKINS_GIT_CLIENT_VERSION/git-client.hpi

ENV JENKINS_SCM_API_VERSION 0.2

RUN curl -sSL --create-dirs -o /usr/share/jenkins/plugins/scm-api.hpi https://updates.jenkins-ci.org/download/plugins/scm-api/$JENKINS_SCM_API_VERSION/scm-api.hpi

ENV JENKINS_GIT_VERSION 2.3.2

RUN curl -sSL --create-dirs -o /usr/share/jenkins/plugins/git.hpi https://updates.jenkins-ci.org/download/plugins/git/$JENKINS_GIT_VERSION/git.hpi

