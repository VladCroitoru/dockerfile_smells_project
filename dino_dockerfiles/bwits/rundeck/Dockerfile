FROM centos:centos6.7

MAINTAINER Bill W

ENV REFRESHED_AT 20160308

ENV JAVA_VERSION=1.7.0
ENV RUNDECK_VERSION=2.6.4-1.15.GA
ENV EC2_PLUG_VERSION=1.5.2

# Install puppet
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-6.noarch.rpm
RUN yum -y update && \
    yum -y install puppet hiera facter 

# Install java and rundeck 
RUN puppet resource package puppet ensure=latest
RUN puppet resource package facter ensure=latest
RUN puppet resource package hiera  ensure=latest
RUN puppet resource package wget   ensure=latest
RUN puppet resource package java-${JAVA_VERSION}-openjdk ensure=latest
RUN puppet resource yumrepo bintray-rundeck baseurl='http://dl.bintray.com/rundeck/rundeck-rpm/' descr='bintray rundeck repo' enabled='1' gpgcheck='0' priority='1'
RUN puppet resource package rundeck ensure=${RUNDECK_VERSION}

# Install rundeck aws ec2 node plugin
RUN wget https://github.com/rundeck-plugins/rundeck-ec2-nodes-plugin/releases/download/v${EC2_PLUG_VERSION}/rundeck-ec2-nodes-plugin-${EC2_PLUG_VERSION}.jar -O /var/lib/rundeck/libext/rundeck-ec2-nodes-plugin-${EC2_PLUG_VERSION}.jar

# Run rundeck
CMD source /etc/rundeck/profile && ${JAVA_HOME:-/usr}/bin/java ${RDECK_JVM} -cp ${BOOTSTRAP_CP} com.dtolabs.rundeck.RunServer /var/lib/rundeck ${RDECK_HTTP_PORT}
