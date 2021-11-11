FROM ubuntu:14.04
MAINTAINER Ernesto Hernandez "ehdez73@gmail.com"

EXPOSE 9000
EXPOSE 9092
EXPOSE 8080

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update

############################################################ BUILD TOOLS #########################################################
# GIT
#####
RUN apt-get install -y git

# JAVA
############
# Auto-accept the Oracle JDK license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections; \
    apt-get install -y oracle-java8-installer

# Node & npm
#########################
RUN apt-get install -q -y nodejs npm; \
    ln -s /usr/bin/nodejs /usr/bin/node;

# grunt, gulp & bower
#########################
RUN npm install -g gulp grunt bower

# Gradle Settings
#################
ADD gradle.properties /root/.gradle/gradle.properties


# PhantomJS 2.0 (headless)
###########################
ADD https://github.com/Pyppe/phantomjs2.0-ubuntu14.04x64/raw/master/bin/phantomjs /usr/local/bin/phantomjs
RUN chmod +x /usr/local/bin/phantomjs
#RUN apt-get install -q -y build-essential g++ flex bison gperf ruby perl libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev libpng-dev libjpeg-dev

RUN apt-get install -q -y libicu52 libfontconfig libfontconfig1 libjpeg8 libpng12-0


############################################################ JENKINS  ############################################################
ENV JENKINS_VERSION 1.647
##########################
ADD http://mirrors.jenkins-ci.org/war/$JENKINS_VERSION/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war

# Plugins
##########
ENV JENKINS_HOME /jenkins
ENV JENKINS_PLUGINS_LOCAL $JENKINS_HOME/plugins
ENV JENKINS_PLUGINS_REMOTE https://updates.jenkins-ci.org/download/plugins

ADD $JENKINS_PLUGINS_REMOTE/build-pipeline-plugin/1.4.9/build-pipeline-plugin.hpi   $JENKINS_PLUGINS_LOCAL/build-pipeline-plugin.hpi
ADD $JENKINS_PLUGINS_REMOTE/git/2.4.2/git.hpi                                       $JENKINS_PLUGINS_LOCAL/git.hpi
ADD $JENKINS_PLUGINS_REMOTE/git-client/1.19.3/git-client.hpi                        $JENKINS_PLUGINS_LOCAL/git-client.hpi
ADD $JENKINS_PLUGINS_REMOTE/jquery/1.11.2-0/jquery.hpi                              $JENKINS_PLUGINS_LOCAL/jquery.hpi
ADD $JENKINS_PLUGINS_REMOTE/parameterized-trigger/2.30/parameterized-trigger.hpi    $JENKINS_PLUGINS_LOCAL/parameterized-trigger.hpi
ADD $JENKINS_PLUGINS_REMOTE/token-macro/1.12.1/token-macro.hpi                      $JENKINS_PLUGINS_LOCAL/token-macro.hpi
ADD $JENKINS_PLUGINS_REMOTE/scm-api/1.0/scm-api.hpi                                 $JENKINS_PLUGINS_LOCAL/scm-api.hpi
ADD $JENKINS_PLUGINS_REMOTE/conditional-buildstep/1.3.3/conditional-buildstep.hpi   $JENKINS_PLUGINS_LOCAL/conditional-buildstep.hpi
ADD $JENKINS_PLUGINS_REMOTE/run-condition/1.0/run-condition.hpi                     $JENKINS_PLUGINS_LOCAL/run-condition.hpi
ADD $JENKINS_PLUGINS_REMOTE/copyartifact/1.37/copyartifact.hpi                      $JENKINS_PLUGINS_LOCAL/copyartifact.hpi
ADD $JENKINS_PLUGINS_REMOTE/promoted-builds/2.24.1/promoted-builds.hpi              $JENKINS_PLUGINS_LOCAL/promoted-builds.hpi
ADD $JENKINS_PLUGINS_REMOTE/ansicolor/0.4.2/ansicolor.hpi                           $JENKINS_PLUGINS_LOCAL/ansicolor.hpi
ADD $JENKINS_PLUGINS_REMOTE/groovy-postbuild/2.3.1/groovy-postbuild.hpi             $JENKINS_PLUGINS_LOCAL/groovy-postbuild.hpi

############################################################ SONAR  ############################################################
ENV SONAR_VERSION 5.3_all
###########################
ADD http://sourceforge.net/projects/sonar-pkg/files/deb/binary/sonar_$SONAR_VERSION.deb/download /tmp/sonar.deb
RUN dpkg -i /tmp/sonar.deb; \
    rm /tmp/sonar.deb

# Plugins
##########
ENV SONAR_PLUGINS_REMOTE https://sonarsource.bintray.com/Distribution
ENV SONAR_PLUGINS_LOCAL /opt/sonar/extensions/plugins

ADD $SONAR_PLUGINS_REMOTE/sonar-javascript-plugin/sonar-javascript-plugin-2.10.jar                    $SONAR_PLUGINS_LOCAL/sonar-javascript-plugin-2.10.jar
ADD $SONAR_PLUGINS_REMOTE/sonar-groovy-plugin/sonar-groovy-plugin-1.3.1.jar                           $SONAR_PLUGINS_LOCAL/sonar-groovy-plugin-1.3.1.jar
ADD https://github.com/emrehan/sonar-scalastyle/releases/download/v0.0.1-SNAPSHOT/sonar-scalastyle-plugin-0.0.1-SNAPSHOT.jar $SONAR_PLUGINS_LOCAL/sonar-scalastyle-plugin-0.0.1-SNAPSHOT.jar
############################################################ ENTRY POINT  ############################################################
ADD run.sh /root/run.sh
RUN chmod +x /root/run.sh

ENTRYPOINT ["/root/run.sh"]
