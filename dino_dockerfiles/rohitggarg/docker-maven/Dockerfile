FROM nimmis/java-centos:oracle-8-jdk

MAINTAINER rohitgarg19@gmail.com
ARG MAVEN_VERSION=3.3.9
ARG MAVEN_HOME="/usr/share/maven"
ARG USER_HOME="/root"

RUN wget http://www-eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz
RUN tar -xzf apache-maven-$MAVEN_VERSION-bin.tar.gz -C /
RUN ln -s /apache-maven-$MAVEN_VERSION $MAVEN_HOME

ENV MAVEN_HOME "$MAVEN_HOME"
ENV MAVEN_CONFIG "$USER_HOME/.m2"
ENV JAVA_HOME /usr

RUN ln -s "$MAVEN_HOME/bin/mvn" /usr/bin/mvn

RUN mkdir -p "$USER_HOME/.m2"
RUN chmod 775 "$USER_HOME/.m2"

ENTRYPOINT ["mvn"]
