FROM ubuntu:14.04

MAINTAINER Jainish Shah <Jainish.shah@getzephyr.com>

RUN \
apt-get update && \
apt-get install -y openjdk-7-jdk && \
rm -rf /var/lib/apt/lists/*

# Define working directory.

WORKDIR /data

# Define commonly used JAVA_HOME variable

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN javac -version

RUN sudo sh -c 'echo "deb http://sdkrepo.atlassian.com/debian/ stable contrib" >>/etc/apt/sources.list'

RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B07804338C015B73

RUN sudo apt-get update

RUN sudo apt-get install atlassian-plugin-sdk

RUN atlas-version

RUN atlas-run-standalone --product jira --version 6.4-OD-05-009 --bundled-plugins com.atlassian.jwt:jwt-plugin:1.1.0,com.atlassian.bundles:json-schema-validator-atlassian-bundle:1.0.4,com.atlassian.webhooks:atlassian-webhooks-plugin:1.0.6,com.atlassian.upm:atlassian-universal-plugin-manager-plugin:2.17.14-D20140902T224549,com.atlassian.plugins:atlassian-connect-plugin:1.1.4 --jvmargs -Datlassian.upm.on.demand=true

ADD tomcat.sh /data/amps-standalone/

RUN chmod 777 /data/amps-standalone/target/container/tomcat7x/apache-tomcat-7.0.40/bin/catalina.sh

RUN chmod -R 755 /data/amps-standalone/tomcat.sh

CMD cd /data/amps-standalone && sudo sh tomcat.sh && tail -f /data/amps-standalone/target/jira-LATEST.log


EXPOSE 2990
