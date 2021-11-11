
FROM java:openjdk-7-jdk
# originally based on UNB Libraries Dockerfile
MAINTAINER Andrew Jackson "anj@anjackson.net"

# update packages and install maven
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y tar wget curl git maven

# move to /opt and download the tomcat package
RUN cd /opt && wget -q "http://www.mirrorservice.org/sites/ftp.apache.org/tomcat/tomcat-7/v7.0.79/bin/apache-tomcat-7.0.79.tar.gz" && \
    cd /opt && tar -zxvf apache-tomcat-7.0.79.tar.gz && \
    cd /opt && ln -sf apache-tomcat-7.0.79 tomcat

# make tomcat scripts executable
RUN chmod +x /opt/tomcat/bin/*.sh

# Cleanup webapps directory
RUN cd /opt/tomcat/webapps && rm -rf *

# Tweak Tomcat configuration
COPY docker/server.xml /opt/tomcat/conf/server.xml
COPY docker/logging.properties /opt/tomcat/conf/logging.properties

# Install ICU4J in the system JVM for broader language support
RUN \
  curl -O http://download.icu-project.org/files/icu4j/58.2/icu4j-58_2.jar && \
  curl -O http://download.icu-project.org/files/icu4j/58.2/icu4j-localespi-58_2.jar && \ 
  mv icu4j-* /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/

# Build UKWA Wayback versions inside the container...
# Need a patched OpenWayback instance:
RUN \
  git clone https://github.com/ukwa/openwayback.git && \
  cd openwayback && \
  git checkout restore-locale-switch && \
  mvn install -DskipTests
  
# Now build our overlays:
COPY . /waybacks
RUN \
  cd waybacks && \
  mvn install -DskipTests

# Define runtime properties

EXPOSE 8080 8090

ENV JAVA_OPTS -Xmx1g

# Use oukwa|ldukwa|qa for Open UKWA, LD UKWA or QA UKWA versions
ENV UKWA_OWB_VERSION=qa 

VOLUME /data

#Fire up tomcat, copying desired WAR into place first
COPY docker/start.sh /

CMD /start.sh


