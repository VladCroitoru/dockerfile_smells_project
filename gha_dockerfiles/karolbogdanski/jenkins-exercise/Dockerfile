FROM jenkins/jenkins:lts-jdk11

USER root

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml

COPY jenkins-config/plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY jobs /usr/local/jobs
COPY jenkins-config/init.groovy /usr/share/jenkins/ref/init.groovy.d/init.groovy
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

COPY jenkins-config/casc.yaml /var/jenkins_home/casc.yaml
