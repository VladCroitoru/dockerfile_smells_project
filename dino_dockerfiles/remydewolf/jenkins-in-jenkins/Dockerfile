FROM jenkins/jenkins:2.95
USER root

# Install docker
RUN apt-get update
RUN apt-get install -y \
	software-properties-common \
	apt-transport-https
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"
RUN apt-get update
RUN apt-get install -y docker-ce

# Configure Jenkins
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV JENKINS_REF /usr/share/jenkins/ref
COPY init.groovy.d/* $JENKINS_REF/init.groovy.d/
COPY jobs $JENKINS_REF/jobs/
