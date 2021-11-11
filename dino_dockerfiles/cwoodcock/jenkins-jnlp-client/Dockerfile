FROM fabric8/java-centos-openjdk8-jre

RUN yum install -y git

ENV HOME /home/jenkins
ENV JENKINS_HOME /home/jenkins

RUN useradd -c "Jenkins user" -d $HOME -m jenkins

RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar http://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/2.52/remoting-2.52.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

COPY start.sh /usr/local/bin/start.sh
WORKDIR /home/jenkins


ENTRYPOINT ["/usr/local/bin/start.sh"]
