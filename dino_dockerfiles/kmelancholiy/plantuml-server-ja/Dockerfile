# docker build -t kmelancholiy/plantuml-server-ja .

FROM tomcat:8.0
MAINTAINER kmelancholiy <kmelancholiy@gmail.com>

# Remove existing wars
RUN rm -r /usr/local/tomcat/webapps/*

# Make dot executable available
ENV DEBIAN_FRONTEND noninteractive
RUN \
  apt-get update &&\
  apt-get install -y graphviz fonts-takao &&\
  apt-get clean &&\
  apt-get autoremove -y &&\
  rm -rf /var/cache/apt/*

# Install plantuml
RUN wget http://sourceforge.net/projects/plantuml/files/plantuml.war/download -O /usr/local/tomcat/webapps/ROOT.war

# Prevent startup taking minutes (http://wiki.apache.org/tomcat/HowTo/FasterStartUp, http://stackoverflow.com/questions/26431922/tomcat7-starts-too-late-on-ubuntu-14-04-x64-digitalocean)
ENV JAVA_PATH /usr/lib/jvm/java-7-openjdk-amd64
RUN sed -i 's|securerandom.source=file:/dev/urandom|securerandom.source=file:/dev/./urandom|' $JAVA_PATH/jre/lib/security/java.security
