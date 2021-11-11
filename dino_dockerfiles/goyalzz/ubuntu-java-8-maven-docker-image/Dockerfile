# Reference URL: https://runnable.com/docker/java/dockerize-your-java-application
# Reference URL: https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/
# Reference URL: https://hub.docker.com/r/mcpayment/ubuntu1404-java8/~/dockerfile/
# Reference URL: https://github.com/TexaiCognitiveArchitecture/docker-java8-jenkins-maven-git-nano
# Reference URL: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#apt-get
# Reference Command: docker search ubuntu/java

# Download base image ubuntu 14.04
FROM ubuntu:trusty

MAINTAINER  Ankush Goyal <ankush.goyal@prontoitlabs.com>
 
# Prepare installation of Oracle Java 8
ENV JAVA_VER 8
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install git, wget, Oracle Java8
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe' >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \
    apt-get update && \
    apt-get install -y git wget && \
    echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y --force-yes --no-install-recommends oracle-java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer

# Set Oracle Java as the default Java
RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# Install maven 3.3.9
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9-bin.tar.gz http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
    tar xzf /tmp/apache-maven-3.3.9-bin.tar.gz -C /opt/ && \
    ln -s /opt/apache-maven-3.3.9 /opt/maven && \
    ln -s /opt/maven/bin/mvn /usr/local/bin  && \
    rm -f /tmp/apache-maven-3.3.9-bin.tar.gz

ENV MAVEN_HOME /opt/maven

EXPOSE 80 443
