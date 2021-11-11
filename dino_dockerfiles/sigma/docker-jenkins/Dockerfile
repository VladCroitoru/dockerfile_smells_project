FROM ubuntu:12.04
MAINTAINER Yann Hodique yann.hodique@gmail.com
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe multiverse" > /etc/apt/sources.list
RUN echo "deb-src http://archive.ubuntu.com/ubuntu precise main universe multiverse" >> /etc/apt/sources.list
RUN apt-get update
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y wget openjdk-6-jre-headless git-core
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" > /etc/apt/sources.list.d/jenkins.list
RUN apt-get update
RUN RUNLEVEL=1 DEBIAN_FRONTEND=1 apt-get install -y jenkins
# RUN (wget --output-document=/usr/local/bin/docker https://get.docker.io/builds/Linux/x86_64/docker-latest && chmod +x /usr/local/bin/docker)
RUN mkdir -p /var/lib/jenkins/plugins
ADD http://updates.jenkins-ci.org/latest/cobertura.hpi /var/lib/jenkins/plugins/cobertura.hpi
ADD http://updates.jenkins-ci.org/latest/greenballs.hpi /var/lib/jenkins/plugins/greenballs.hpi
ADD http://updates.jenkins-ci.org/latest/instant-messaging.hpi /var/lib/jenkins/plugins/instant-messaging.hpi
ADD http://updates.jenkins-ci.org/latest/ircbot.hpi /var/lib/jenkins/plugins/ircbot.hpi
ADD http://updates.jenkins-ci.org/latest/postbuild-task.hpi /var/lib/jenkins/plugins/postbuild-task.hpi
ADD http://updates.jenkins-ci.org/latest/copy-to-slave.hpi /var/lib/jenkins/plugins/copy-to-slave.hpi
ADD http://updates.jenkins-ci.org/latest/credentials.hpi /var/lib/jenkins/plugins/credentials.hpi
ADD http://updates.jenkins-ci.org/latest/ssh-credentials.hpi /var/lib/jenkins/plugins/ssh-credentials.hpi
ADD http://updates.jenkins-ci.org/latest/ssh-agent.hpi /var/lib/jenkins/plugins/ssh-agent.hpi
ADD http://updates.jenkins-ci.org/latest/git-client.hpi /var/lib/jenkins/plugins/git-client.hpi
ADD http://updates.jenkins-ci.org/latest/git.hpi /var/lib/jenkins/plugins/git.hpi
ADD http://updates.jenkins-ci.org/latest/scm-api.hpi /var/lib/jenkins/plugins/scm-api.hpi

ENV JENKINS_HOME /var/lib/jenkins

EXPOSE 8080
VOLUME /var/lib/jenkins
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]
