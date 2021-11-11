FROM ubuntu:14.04
MAINTAINER Pitchanon Dumrongsiri <Pitchanon.D@gmail.com>

# Install Jenkins
RUN apt-get update
RUN echo deb http://pkg.jenkins.io/debian-stable binary/ >> /etc/apt/sources.list.d/jenkins.list
RUN apt-get install -y wget
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN apt-get update
RUN apt-get install -y jenkins \
    git \
    make \
    gcc \
    curl && \
    rm -rf /var/lib/apt/lists/*
ENV JENKINS_HOME /var/jenkins_home

# Install go
ENV GOLANG_VERSION 1.7
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ADD $GOLANG_DOWNLOAD_URL /tmp/
RUN tar -xvf /tmp/go$GOLANG_VERSION.linux-amd64.tar.gz -C /usr/local && \
    rm /tmp/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOROOT=/usr/local/go
ENV GOBIN=$GOROOT/bin
ENV PATH=$PATH:$GOBIN
ENV GOPATH=/var/jenkins_home/workspace/go

# Make sure we exec to pass on signals correctly
CMD exec java -jar /usr/share/jenkins/jenkins.war
