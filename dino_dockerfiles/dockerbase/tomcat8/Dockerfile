# VERSION 1.0
# DOCKER-VERSION  1.2.0
# AUTHOR:         Richard Lee <lifuzu@gmail.com>
# DESCRIPTION:    Tomcat Image Container

FROM dockerbase/service-java8

MAINTAINER Richad Lee "lifuzu@gmail.com"

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

# Information Of Package
ENV	PKG_VERSION apache-tomcat-8.0.12
ENV	PKG_PACKAGE $PKG_VERSION.tar.gz
ENV	PKG_LINK http://supergsego.com/apache/tomcat/tomcat-8/v8.0.12/bin/$PKG_PACKAGE

# Update
RUN     apt-get update

# Java
RUN     cd /tmp && \
        curl -O -L $PKG_LINK && \
        tar -zxf /tmp/$PKG_PACKAGE -C /usr/local && \
        ln -s /usr/local/$PKG_VERSION /usr/local/tomcat

ENV     CATALINA_HOME /usr/local/tomcat
ENV     JAVA_HOME /usr/local/java
ENV     JRE_HOME /usr/local/java/jre
ENV     PATH $PATH:$JAVA_HOME/bin:$JRE_HOME/bin:$CATALINA_HOME/bin

RUN     mkdir -p /etc/service/tomcat
ADD     build/runit/tomcat /etc/service/tomcat/run

# clean up
RUN     apt-get clean
RUN     rm -rf /tmp/* /var/tmp/*
RUN     rm -rf /var/lib/apt/lists/*

# Set volume
VOLUME ["/usr/local/tomcat/webapps"]

# for main web interface:                                                         
EXPOSE  8080 

# Set environment variables.
ENV     HOME /root

# Define working directory.
WORKDIR /root

# Define default command.
CMD ["bash"]
