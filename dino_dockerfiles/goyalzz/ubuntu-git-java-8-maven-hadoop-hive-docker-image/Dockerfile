# Reference URL: https://runnable.com/docker/java/dockerize-your-java-application
# Reference URL: https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/
# Reference URL: https://hub.docker.com/r/mcpayment/ubuntu1404-java8/~/dockerfile/
# Reference URL: https://github.com/TexaiCognitiveArchitecture/docker-java8-jenkins-maven-git-nano
# Reference URL: https://github.com/kurron/docker-sts/blob/master/Dockerfile
# Reference Command: docker search ubuntu/java

# Download base image ubuntu 16.04
FROM goyalzz/ubuntu:latest

MAINTAINER  Ankush Goyal <ankush.goyal@prontoitlabs.com>

LABEL org.goyalzz.ide.name="Spring Tool Suite" org.goyalzz.ide.version=3.7.2
 
# Update Software repository
RUN apt-get update

# Install Git
RUN apt-get install -y git

# Update the package repository
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update

# Install Oracle Java 8
ENV JAVA_VER 8
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \
    apt-get update && \
    echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y --force-yes --no-install-recommends oracle-java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \
    apt-get clean && \
    rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer

# Set Oracle Java as the default Java
RUN update-java-alternatives -s java-8-oracle

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# Clean Up APT when finished
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update dpkg repositories
RUN apt-get update 

# Install wget
RUN apt-get install -y wget

# Get maven 3.3.9
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9-bin.tar.gz http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz

# Install maven
RUN tar xzf /tmp/apache-maven-3.3.9-bin.tar.gz -C /opt/
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven
RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.3.9-bin.tar.gz
ENV MAVEN_HOME /opt/maven

# Update Software repository
RUN apt-get update

# Download Spring-Tool-Suit (v3.8.4.RELEASE)
ADD http://download.springsource.com/release/STS/3.8.4.RELEASE/dist/e4.6/spring-tool-suite-3.8.4.RELEASE-e4.6.3-linux-gtk-x86_64.tar.gz /tmp/ide.tar.gz

# Install STS
RUN mkdir -p /opt/ide && \
    tar zxvf /tmp/ide.tar.gz --strip-components=1 -C /opt/ide && \
    ln -s /usr/lib/jvm/jdk1.8.0_65/jre /opt/ide/sts-3.7.2.RELEASE/jre && \
    chown -R developer:developer /opt/ide && \
    rm /tmp/ide.tar.gz && \
    apt-get update && \
    apt-get install -y libxslt1.1 && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

USER developer:developer
WORKDIR /home/developer
ENTRYPOINT ["/opt/ide/sts-3.7.2.RELEASE/STS"]
EXPOSE 8080
