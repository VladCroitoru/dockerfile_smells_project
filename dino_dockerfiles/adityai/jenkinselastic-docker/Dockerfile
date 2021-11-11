FROM jenkins
MAINTAINER Aditya Inapurapu at iaditya.com

COPY ./jenkins_home /var/jenkins_home

COPY ./elasticsearch_home/config /usr/share/elasticsearch/config

RUN wget -P /var/jenkins_home/plugins http://updates.jenkins-ci.org/latest/logstash.hpi
