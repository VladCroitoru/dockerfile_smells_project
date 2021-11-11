FROM jenkins
MAINTAINER Bahadir Yagan <bahadir.yagan@gmail.com>

USER root

RUN apt-get update
RUN apt-get install -y apparmor \
        git \
        mercurial \
        docker.io

# Setup Maven
ENV MAVEN_VERSION 3.3.3

RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
COPY settings.xml /root/.m2/settings.xml

# Confiure Jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
COPY config.groovy /usr/share/jenkins/ref/init.groovy.d/config.groovy
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

# Volumes
VOLUME /root/.ssh

# Start it all
COPY init.sh /usr/local/bin/init.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/init.sh"]
