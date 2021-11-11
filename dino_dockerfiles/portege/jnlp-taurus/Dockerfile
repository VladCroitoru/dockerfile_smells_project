# blazemeter section
FROM blazemeter/taurus

MAINTAINER Boyke Dian Triwahyudhi <boi@mas-mas.it>
RUN mkdir -p /tmp/artifacts/
RUN chmod 777 /tmp/artifacts/

# jenkinsci/slave
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | \
  debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | \
  debconf-set-selections
RUN apt-get install oracle-java8-installer -y

ENV HOME /home/jenkins
RUN addgroup --system --gid 10000 jenkins
RUN adduser --system -u 10000 --home $HOME --ingroup jenkins jenkins
LABEL Description="This is a base image, which provides the Jenkins agent executable (slave.jar)" Vendor="Jenkins project" Version="3.14"

ARG VERSION=3.14
ARG AGENT_WORKDIR=/home/jenkins/agent

RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

USER jenkins
ENV AGENT_WORKDIR=${AGENT_WORKDIR}
RUN mkdir /home/jenkins/.jenkins && mkdir -p ${AGENT_WORKDIR}

VOLUME /home/jenkins/.jenkins
VOLUME ${AGENT_WORKDIR}
WORKDIR /home/jenkins


# jenkinsci/docker-jnlp-slave
# MAINTAINER Nicolas De Loof <nicolas.deloof@gmail.com>
# https://github.com/jenkinsci/docker-jnlp-slave.git

COPY jenkins-slave /usr/local/bin/jenkins-slave

ENTRYPOINT ["jenkins-slave"]
