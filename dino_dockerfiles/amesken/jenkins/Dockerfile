FROM jenkins:1.625.2

MAINTAINER Andries Mesken <andries.mesken@ziggo.nl>

USER root

ENV JAVA_OPTS="-Xmx4G -Xms2G"
ENV JENKINS_OPTS="--handlerCountStartup=50 --handlerCountMax=150"
ENV JENKINS_HOME="/var/jenkins_home"
ENV JENKINS_SHARED_REFERENCE="/usr/share/jenkins/ref"
ENV GROOVY_VERSION="2.4.5"

############################################
# Configure Jenkins
############################################
# Adding plugins
COPY plugins.txt $JENKINS_HOME/plugins.txt
RUN /usr/local/bin/plugins.sh $JENKINS_HOME/plugins.txt

# Adding default Jenkins Jobs
COPY jobs/1-github-seed-job.xml $JENKINS_SHARED_REFERENCE/jobs/1-github-seed-job/config.xml
COPY jobs/2-job-dsl-seed-job.xml $JENKINS_SHARED_REFERENCE/jobs/2-job-dsl-seed-job/config.xml
COPY jobs/3-conference-app-seed-job.xml $JENKINS_SHARED_REFERENCE/jobs/3-conference-app-seed-job/config.xml
COPY jobs/4-selenium2-maven-test.xml $JENKINS_SHARED_REFERENCE/jobs/4-selenium2-maven-test/config.xml
COPY jobs/6-conference-app-ci.xml $JENKINS_SHARED_REFERENCE/jobs/conference-app-1-ci/config.xml
COPY jobs/6-conference-app-sonar-analysis.xml $JENKINS_SHARED_REFERENCE/jobs/conference-app-2-sonar-analysis/config.xml
COPY jobs/7-conference-app-monitoring-ci.xml $JENKINS_SHARED_REFERENCE/jobs/conference-app-monitoring-1-ci/config.xml
COPY jobs/7-conference-app-monitoring-sonar-analysis.xml $JENKINS_SHARED_REFERENCE/jobs/conference-app-monitoring-2-sonar-analysis/config.xml

# Jenkins settings
COPY config/config.xml $JENKINS_SHARED_REFERENCE/config.xml

# Jenkins Settings, i.e. Maven, Groovy, ...
COPY config/hudson.tasks.Maven.xml $JENKINS_SHARED_REFERENCE/hudson.tasks.Maven.xml
COPY config/hudson.plugins.groovy.Groovy.xml $JENKINS_SHARED_REFERENCE/hudson.plugins.groovy.Groovy.xml
COPY config/maven-global-settings-files.xml $JENKINS_SHARED_REFERENCE/maven-global-settings-files.xml

# SSH Keys & Credentials
COPY config/credentials.xml $JENKINS_SHARED_REFERENCE/credentials.xml
COPY config/ssh-keys/id_rsa $JENKINS_SHARED_REFERENCE/.ssh/id_rsa
COPY config/ssh-keys/id_rsa.pub $JENKINS_SHARED_REFERENCE/.ssh/id_rsa.pub

# Switch to root user to change jenkins group and get groovy
USER root
# http://dl.bintray.com/groovy/maven/apache-groovy-binary-2.4.5.zip
RUN \ 
  curl -L -o groovy.zip https://bintray.com/artifact/download/groovy/maven/apache-groovy-binary-$GROOVY_VERSION.zip && \
  unzip -fo groovy.zip -d /usr/share/groovy-$GROOVY_VERSION && \
  rm groovy.zip
RUN mkdir -p /c/Users/Andries/docker/data/jenkins && chmod 777 /c/Users/Andries/docker/data/jenkins && usermod -g root jenkins

VOLUME ["$JENKINS_HOME"]