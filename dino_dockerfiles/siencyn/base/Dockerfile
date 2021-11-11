#Dockerfile for the siencyn base image for Jenkins, based on the Alpine Linux image

FROM alpine:3.1

MAINTAINER Manuel Weidmann <weidmann.manuel@gmail.com>

RUN apk add --update openjdk7-jre-base \
    ttf-dejavu \
    && rm -rf /var/cache/apk/* \
    && wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war \
    && mv jenkins.war /home/jenkins.war \
    && mkdir /home/jenkins

ENV JENKINS_HOME /home/jenkins
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk
ENV JAVA $JAVA_HOME/bin
ENV PATH $PATH:$JAVA_HOME:$JAVA

WORKDIR /home

ENTRYPOINT ["java", "-Djava.awt.headless=true", "-jar", "/home/jenkins.war"]
