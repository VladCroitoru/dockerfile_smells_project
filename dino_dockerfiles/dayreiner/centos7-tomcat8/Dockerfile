FROM centos:latest
MAINTAINER dayreiner

# Tomcat and Java Vars
ENV JDK_MAJOR_VERSION=8u74 \
    JDK_VERSION=1.8.0_74 \
    TOMCAT_MAJOR_VERSION=8 \
    TOMCAT_VERSION=8.0.38 \
    JAVA_HOME=/opt/java \
    CATALINA_HOME=/opt/tomcat \
    PATH=$PATH:$JAVA_HOME/bin:${CATALINA_HOME}/bin:${CATALINA_HOME}/scripts \
    JAVA_OPTS="-Xms512m -Xmx2048m"

# Update and install latest packages and prerequisites
RUN yum -y update && yum clean all && yum -y install wget
    
COPY config/ /opt/

# Install Oracle JDK and Tomcat
RUN echo "Installing Java JDK ${JDK_VERSION}..." && \
    cd /opt && \
    wget -nv --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/${JDK_MAJOR_VERSION}-b02/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz \
    -O /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    echo "Checking file integrity..." && \
    sha1sum -c /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz.sha && \
    tar xf /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    rm jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    mv jdk${JDK_VERSION} ${JAVA_HOME} && \
    echo "Installing Tomcat ${TOMCAT_VERSION}..." && \
    wget -nv http://apache.mirror.gtcomm.net/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz \
    -O /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    echo "Checking file integrity..." && \
    sha1sum -c /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz.sha && \
    tar xf /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm  apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    mv apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME} && \
    chmod +x ${CATALINA_HOME}/bin/*sh

# Tomcat scripts setup
COPY scripts/ ${CATALINA_HOME}/scripts/
RUN chmod +x ${CATALINA_HOME}/scripts/*.sh

# Expose and Start Services
WORKDIR ${CATALINA_HOME}
EXPOSE 8080 8009
CMD ["/opt/tomcat/scripts/tomcat.sh"]
