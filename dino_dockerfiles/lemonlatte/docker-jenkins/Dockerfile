FROM ubuntu:14.04
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN apt-get update
RUN apt-get -qqy install supervisor curl
RUN curl http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list
RUN apt-get update

# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407
RUN mkdir /var/run/jenkins
RUN apt-get install -qqy jenkins=1.598

# Fix Java AWT headless problem:
# https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+got+java.awt.headless+problem
RUN apt-get install -qqy ttf-dejavu

# Clean apt cache files
RUN apt-get clean -qqy

# Fix timezone in container
RUN echo "Asia/Taipei" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

ADD supervisor-jenkins.conf /etc/supervisor/conf.d/
ADD bootstrap.sh /

EXPOSE 8080
VOLUME ["/var/lib/jenkins"]
CMD ["/bootstrap.sh"]
