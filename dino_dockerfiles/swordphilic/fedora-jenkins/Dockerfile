FROM fedora:latest
MAINTAINER Navid Shaikh <nshaikh@redhat.com>

RUN dnf -y update; dnf -y install java; dnf -y install wget
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key
RUN dnf -y install jenkins

EXPOSE 8080

VOLUME ["/root/.jenkins"]

CMD ["/usr/bin/java", "-jar", "/usr/lib/jenkins/jenkins.war", "--webroot=/root/.jenkins/web"]
