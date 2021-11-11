FROM ubuntu

MAINTAINER Sandor Zelei

# Install JDK 8
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && apt-get update && apt-get install -y oracle-java8-installer ca-certificates

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Get Tomcat
RUN wget --quiet --no-cookies http://xenia.sote.hu/ftp/mirrors/www.apache.org/tomcat/tomcat-8/v8.0.33/bin/apache-tomcat-8.0.33.tar.gz -O /tmp/tomcat.tgz

# Uncompress
RUN tar xzvf /tmp/tomcat.tgz -C /opt
RUN mv /opt/apache-tomcat-8.0.33 /opt/tomcat
RUN rm /tmp/tomcat.tgz

# Remove garbage
RUN rm -rf /opt/tomcat/webapps/examples
RUN rm -rf /opt/tomcat/webapps/docs
RUN rm -rf /opt/tomcat/webapps/ROOT

ADD setenv.sh /opt/tomcat/bin

# Add keystore
ADD .keystore /root

RUN wget --quiet --no-cookies http://central.maven.org/maven2/com/mchange/c3p0/0.9.5.2/c3p0-0.9.5.2.jar -P /opt/tomcat/lib
RUN wget --quiet --no-cookies http://central.maven.org/maven2/com/mchange/mchange-commons-java/0.2.11/mchange-commons-java-0.2.11.jar -P /opt/tomcat/lib
RUN wget --quiet --no-cookies http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.38/mysql-connector-java-5.1.38.jar -P /opt/tomcat/lib


ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

EXPOSE 80
EXPOSE 8080
EXPOSE 8009

VOLUME ["/opt/tomcat/conf","/opt/tomcat/logs","/opt/tomcat/configuration","/opt/tomcat/media","/opt/tomcat/app"]

WORKDIR /opt/tomcat