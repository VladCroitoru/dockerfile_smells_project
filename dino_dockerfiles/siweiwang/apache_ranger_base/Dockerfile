FROM centos:centos7


# Build packages
RUN yum clean all -y && \
      yum update -y && \
      yum -y install vim wget rpm-build which tar git gcc

# Install Orcale JAVA 8
RUN   wget --no-check-certificate --no-cookies --header "Cookie:oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.rpm -O jdk-8u60-linux-x64.rpm && \
      rpm -Uvh jdk-8u60-linux-x64.rpm

ENV JAVA_HOME /usr/java/default/

# Download apach ranger
RUN mkdir /opt/ranger && \
    export https_proxy=$http_proxy && \
    wget -P /opt/ranger https://dist.apache.org/repos/dist/release/ranger/0.7.0/apache-ranger-0.7.0.tar.gz && \
    tar -zxvf /opt/ranger/apache-ranger-0.7.0.tar.gz -C /opt/ranger

# Install maven
RUN mkdir /opt/maven && \
    export http_proxy=$http_proxy && \
    wget -P /opt/maven http://mirror.dsrg.utoronto.ca/apache/maven/maven-3/3.5.0/binaries/apache-maven-3.5.0-bin.tar.gz && \
    tar -xzvf /opt/maven/apache-maven-3.5.0-bin.tar.gz -C /opt/maven

WORKDIR /opt/ranger/apache-ranger-0.7.0

# Build ranger
RUN /opt/maven/apache-maven-3.5.0/bin/mvn clean package assembly:assembly -DskipTests
