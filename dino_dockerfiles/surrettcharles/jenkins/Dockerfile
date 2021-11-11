FROM jenkins/jenkins:alpine

ENV CONFIG_PATH /jenkins-config
ENV JOB_PATH /jenkins-jobs
ENV JENKINS_HOME /var/jenkins_home
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false
COPY plugins.txt ${CONFIG_PATH}/plugins.txt
COPY scripts/*.groovy $JENKINS_HOME/init.groovy.d/
RUN /usr/local/bin/install-plugins.sh < ${CONFIG_PATH}/plugins.txt
