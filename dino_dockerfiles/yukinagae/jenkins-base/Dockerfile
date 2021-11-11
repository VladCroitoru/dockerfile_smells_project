#
# VERSION 0.0.1
#

FROM centos:centos6
MAINTAINER yukinagae "yuki.nagae1130@gmail.com"

# epel
RUN rpm -ivh http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm

# remi
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm

# update
RUN yum -y update

# basic
RUN yum -y install git
Run yum -y install wget

# java
RUN yum -y install java-1.7.0-openjdk-devel

# jenkins
Run wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
Run rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
Run yum -y install jenkins

# port
EXPOSE 8080

# start jenkins
CMD service jenkins start && tail -f /dev/null
