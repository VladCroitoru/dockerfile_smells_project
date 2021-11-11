FROM jpetazzo/dind
MAINTAINER Yasser Nabi "yassersaleemi@gmail.com"
ENV JENKINS_HOME /jenkins
ENV JENKINS_SWARM_CLIENT_VER 1.15
ENV JENKINS_JAVA_ARGS '-Djava.awt.headless=true'
ENV TZ Europe/London
ENV DEBIAN_FRONTEND noninteractive
EXPOSE 2812 22

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && \
        apt-get update && \
        apt-get -y install \
            openssh-server \
            monit \
            curl \
            openjdk-7-jre-headless \
            git \
            subversion

ADD ./monit.d/ /etc/monit/conf.d/
ADD ./jenkins.sudoers /etc/sudoers.d/jenkins
ADD ./jenkins_init_wrapper.sh /jenkins_init_wrapper.sh
ADD ./start.sh /start.sh

RUN mkdir -p ${JENKINS_HOME} && curl -s -L -o $JENKINS_HOME/swarm-client.jar \
      http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/${JENKINS_SWARM_CLIENT_VER}/swarm-client-${JENKINS_SWARM_CLIENT_VER}-jar-with-dependencies.jar

ENTRYPOINT ["/bin/bash", "/start.sh"]
