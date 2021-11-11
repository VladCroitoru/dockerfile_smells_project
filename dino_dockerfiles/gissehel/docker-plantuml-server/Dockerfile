# docker build -t neam/plantuml-server .

FROM tomcat:8.0
# MAINTAINER Fredrik Wollsén <fredrik@neam.se>
MAINTAINER Gissehel <public-dev-docker-plantuml-server@gissehel.org>

# Remove existing wars
RUN rm -r /usr/local/tomcat/webapps/*

# Make dot executable available
ENV DEBIAN_FRONTEND noninteractive
RUN \
  apt-get update &&\
  apt-get install -y graphviz &&\
  apt-get clean &&\
  apt-get autoremove -y &&\
  rm -rf /var/cache/apt/*

# Install plantuml
RUN wget http://sourceforge.net/projects/plantuml/files/plantuml.war/download -O /usr/local/tomcat/webapps/ROOT.war && \
    wget https://www.dropbox.com/s/z7yah4mpi2mk1mj/plantuml-jlatexmath.zip?dl=0 -O /tmp/plantuml-jlatexmath.zip && \
    mkdir -p /usr/local/tomcat/webapps/ROOT/WEB-INF/lib && \
    unzip /usr/local/tomcat/webapps/ROOT.war -d /usr/local/tomcat/webapps/ROOT && \
    unzip /tmp/plantuml-jlatexmath.zip -d /usr/local/tomcat/webapps/ROOT/WEB-INF/lib && \
    rm -f /tmp/plantuml-jlatexmath.zip

# Prevent startup taking minutes (http://wiki.apache.org/tomcat/HowTo/FasterStartUp, http://stackoverflow.com/questions/26431922/tomcat7-starts-too-late-on-ubuntu-14-04-x64-digitalocean)
ENV JAVA_PATH /usr/lib/jvm/java-7-openjdk-amd64
RUN sed -i 's|securerandom.source=file:/dev/urandom|securerandom.source=file:/dev/./urandom|' $JAVA_PATH/jre/lib/security/java.security
