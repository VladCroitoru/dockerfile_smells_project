FROM centos
MAINTAINER Alessandro Poli <alessandro.poli@mondora.com>

# Configuration variables
ENV JAVA_VERSION 8u92
ENV JAVA_RPM jre-$JAVA_VERSION-linux-x64.rpm
ENV JAVA_RPM_URL http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-b14/$JAVA_RPM
ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.0.47
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
ENV TOMCAT_DEST_PATH /opt
ENV CATALINA_HOME $TOMCAT_DEST_PATH/tomcat
ENV INSTALL_FOLDER install

# Java options
ENV CATALINA_OPTS "-Xms512M -Xmx2048M -server -XX:+UseParallelGC"
ENV JAVA_OPTS "-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom -Djsse.enableSNIExtension=true"

# Install Oracle JRE
RUN yum -y install wget && \
    wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" $JAVA_RPM_URL  -P /tmp && \
    rpm -hiv /tmp/$JAVA_RPM && \
    rm -f /tmp/$JAVA_RPM
# Install Java Crypto Extension
RUN yum -y install unzip && \
    wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip -P /tmp && \
    unzip /tmp/jce_policy-8.zip -d /tmp && \
    mv -f /tmp/UnlimitedJCEPolicyJDK8/* /usr/java/jre1.8.0_92/lib/security/

# Install Tomcat
RUN wget "$TOMCAT_TGZ_URL" -P $TOMCAT_DEST_PATH && \
    tar -xzpf $TOMCAT_DEST_PATH/apache-tomcat-$TOMCAT_VERSION.tar.gz -C $TOMCAT_DEST_PATH && \
    mv $TOMCAT_DEST_PATH/apache-tomcat-$TOMCAT_VERSION $TOMCAT_DEST_PATH/tomcat && \
    rm -f $TOMCAT_DEST_PATH/apache-tomcat-$TOMCAT_VERSION.tar.gz
