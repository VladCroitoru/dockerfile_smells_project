FROM ubuntu:14.04

MAINTAINER Erik Osterman "e@osterman.com"

ENV JENKINS_USER jenkins
ENV JENKINS_SWARM_VERSION 1.22
ENV JENKINS_MASTER_HOST localhost
ENV JENKINS_MASTER_PORT 8080
ENV JENKINS_SLAVE_USERNAME jenkins
ENV JENKINS_SLAVE_PASSWORD password
ENV JENKINS_SLAVE_MODE normal
ENV JENKINS_SLAVE_NAME jenkins-slave
ENV JENKINS_SLAVE_EXECUTORS 1

# System 
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /home/jenkins/
ENV JAVA_OPTS -Xmx1048m -XX:MaxPermSize=512m

USER root
ADD jenkins-slave.sh /opt/jenkins-slave.sh
ADD http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/$JENKINS_SWARM_VERSION/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar /usr/share/jenkins/swarm-client-$JENKINS_SWARM_VERSION-jar-with-dependencies.jar 

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install locales default-jre software-properties-common && \
    apt-add-repository multiverse && \
    apt-get update && \
    apt-get -y install \
                       ruby1.9.1 \
                       rubygems-integration \
                       perl \
                       python-pip python-requests python-docopt \
                       dnsutils \
                       libdbi-perl \
                       libdbd-mysql-perl \
                       libmath-random-perl \
                       libhtml-parser-perl \
                       libxml-rss-perl \
                       libxml-opml-perl \
                       libnet-oauth-perl \
                       libjson-perl \
                       libwww-perl \
                       python-docopt \
                       python-requests \
                       curl \
                       wget \
                       git \
                       mysql-client \
                       maven \
                       default-jre \
                       openjdk-7-jdk \
                    && \
    apt-get clean && \
    useradd -c "Jenkins" -d $HOME -m $JENKINS_USER && \
    chmod 755 /usr/share/jenkins && \
    chmod 644 /usr/share/jenkins/*.jar && \
    sudo usermod -aG sudo $JENKINS_USER && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/nopasswd  && \
    ln -s /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/libdevmapper.so.1.02 && \
    gem install cloudfront-invalidator 

# Locale specific
ENV TIMEZONE Etc/UTC
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen $LANGUAGE && \
    dpkg-reconfigure locales && \
    echo "$TIMEZONE" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata 

USER $JENKINS_USER
ENTRYPOINT /opt/jenkins-slave.sh

