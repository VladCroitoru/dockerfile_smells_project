FROM gomex/wheezy
MAINTAINER Rafael Gomes "gomex@riseup.net"

WORKDIR /var/lib/jenkins

## Jenkins installation

RUN apt-get update && apt-get clean
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y openjdk-7-jre-headless git && apt-get clean
ADD http://mirrors.jenkins-ci.org/war/1.611/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war
VOLUME /var/lib/jenkins

ENV JENKINS_HOME /var/lib/jenkins

## SSH Acess files

ADD id_rsa /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub

## Configuration files

ENV CONF_FOLDER=/root 
ADD credentials.xml $CONF_FOLDER/credentials.xml
ADD config.xml $CONF_FOLDER/config.xml
ADD hudson.tasks.Maven.xml $CONF_FOLDER/hudson.tasks.Maven.xml

## Other parameters

ADD run /usr/local/bin/run

VOLUME /var/lib/jenkins
EXPOSE 8080
CMD /usr/local/bin/run
