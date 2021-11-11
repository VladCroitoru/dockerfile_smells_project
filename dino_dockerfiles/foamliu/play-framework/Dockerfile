FROM centos:7
MAINTAINER Foam Liu <foamliu@yeah.net>

# Install dependencies
ENV ACTIVATOR_VERSION 1.3.7

RUN yum install -y epel-release
RUN yum install -y git make curl wget zip unzip
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel
RUN yum install -y nodejs npm
# Define JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk
WORKDIR /tmp

# Install play
RUN wget http://downloads.typesafe.com/typesafe-activator/${ACTIVATOR_VERSION}/typesafe-activator-${ACTIVATOR_VERSION}.zip && \
    unzip typesafe-activator-${ACTIVATOR_VERSION}.zip && \
    mv activator-dist-${ACTIVATOR_VERSION} /opt/activator && \
    rm typesafe-activator-${ACTIVATOR_VERSION}.zip
RUN echo "export PATH=$PATH:/opt/activator" >> /root/.bashrc	
# Define user home. Activator will store ivy2 and sbt caches on /root/Code volume
RUN echo "export _JAVA_OPTIONS='-Duser.home=/root/Code'" >> /root/.bashrc

# Change user, launch bash
USER root
WORKDIR /root
CMD ["/bin/bash"]

# Expose Code volume and play ports 9000 default 9999 debug 8888 activator ui
VOLUME "/root/Code"
EXPOSE 9000
EXPOSE 9999
EXPOSE 8888
WORKDIR /root/Code