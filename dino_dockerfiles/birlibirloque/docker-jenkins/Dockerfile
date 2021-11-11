FROM jenkinsci/jenkins:2.46.2

COPY install-plugins.sh /usr/local/bin/install-plugins.sh
COPY plugins.txt /usr/share/jenkins/plugins.txt

RUN /usr/local/bin/install-plugins.sh /usr/share/jenkins/plugins.txt

ENV JENKINS_USER admin
ENV JENKINS_PASS admin

RUN echo 2.46.2 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
RUN echo 2.46.2 > /usr/share/jenkins/ref/jenkins.install.InstallUtil.lastExecVersion

# Skip initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false -Djava.net.preferIPv4Stack=true

COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/

VOLUME /var/jenkins_home

