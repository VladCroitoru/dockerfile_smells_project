FROM ubuntu:14.04

MAINTAINER Carlos Moro <cmoro@deusto.es>

ENV TOMCAT_VERSION 8.0.33

# Set locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8

# Fix sh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install dependencies
RUN apt-get update && \
apt-get install -y git build-essential curl wget software-properties-common

# Install JDK 8
RUN \
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
add-apt-repository -y ppa:webupd8team/java && \
apt-get update && \
apt-get install -y oracle-java8-installer wget unzip tar && \
rm -rf /var/lib/apt/lists/* && \
rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Get Tomcat
RUN wget --quiet --no-cookies http://apache.rediris.es/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \
tar xzvf /tmp/tomcat.tgz -C /opt && \
mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat && \
rm /tmp/tomcat.tgz && \
rm -rf /opt/tomcat/webapps/examples && \
rm -rf /opt/tomcat/webapps/docs && \
rm -rf /opt/tomcat/webapps/ROOT

# DO NOT ADD: Add admin/admin user
# ADD tomcat-users.xml /opt/tomcat/conf/

ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

ADD catalina.properties /opt/tomcat/conf
ADD http://projects.iq.harvard.edu/files/fits/files/fits-0.10.2.zip /home
RUN mkdir /tmp/FITS
ADD http://projects.iq.harvard.edu/files/fits/files/fits-1.1.1.war /tmp/FITS/fits.war
RUN cd /tmp/FITS ; jar -xf fits.war ; rm fits.war ; rm index.html
ADD index.html /tmp/FITS/
RUN cd /tmp/FITS ; jar -cf ROOT.war * ; mv ROOT.war /opt/tomcat/webapps/ROOT.war
RUN mkdir /processing
RUN cd /home ; unzip -q fits-0.10.2.zip ; rm /home/fits*zip ; mv /home/fits-* /home/fits

VOLUME ["/processing"]
EXPOSE 8080
EXPOSE 8009
# Removing this volume for FITS: VOLUME "/opt/tomcat/webapps"
WORKDIR /opt/tomcat

# Launch Tomcat
CMD ["/opt/tomcat/bin/catalina.sh", "run"]
