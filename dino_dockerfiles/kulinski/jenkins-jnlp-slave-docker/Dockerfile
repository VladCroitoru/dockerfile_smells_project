FROM java:openjdk-8-jdk-alpine
MAINTAINER Chris Kulinski

# Get a copy of docker executable to use within this container
# also need bash for jenkins slave script
# and need ssh to work with git+ssh urls
RUN apk --no-cache add \
	docker \
	openssh-client \
	bash

# Add all the Jenkins JNLP stuff

ENV HOME /home/jenkins
RUN adduser -h $HOME -D jenkins

RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar http://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/2.59/remoting-2.59.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

COPY jenkins-slave /usr/local/bin/jenkins-slave

VOLUME /home/jenkins
WORKDIR /home/jenkins

# Don't run as jenkins *temporarily* as we work out exposing the docker socket
#USER jenkins

ENTRYPOINT ["jenkins-slave"]
