# version: 3.1
#FROM maxwu/maven-selenium:chrm-ffv1
#FROM maven:3.3.9-jdk-8-onbuild
#FROM openjdk:8-jdk
#FROM maven:latest
#FROM dockerfile/chrome
FROM siomiz/chrome
MAINTAINER maxwu "maxwunj@gmail.com"

ARG MAVEN_VERSION=3.3.9
ARG USER_HOME_DIR="/root"

# Make debconf not in interactive mode
ENV DEBIAN_FRONTEND noninteractive

RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y curl

RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get install -y git
# Install Java8
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install Maven
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

# Set xvfb and VNC
#RUN set -xe \
#    && apt-get update \
#    && apt-get install -y --no-install-recommends ca-certificates curl socat \
#    && apt-get install -y --no-install-recommends xvfb x11vnc fluxbox xterm \
#    && apt-get install -y --no-install-recommends sudo \
#    && apt-get install -y --no-install-recommends supervisor \
#    && rm -rf /var/lib/apt/lists/*

VOLUME "$USER_HOME_DIR/.m2"
#RUN apt-get update
#RUN apt-get install -y git
#RUN mkdir /var/ccm-toy 
#RUN cd /var/ccm-toy
#RUN git clone https://github.com/maxwu/cucumber-java-toy.git
#WORKDIR /var/ccm-toy
RUN uname -a

# Install Chromium.
#RUN \
#  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
#  apt-get update && \
#  apt-get install -y google-chrome-stable && \
#  rm -rf /var/lib/apt/lists/*

RUN \
  echo " \n\
                   /__/__/__/__/__/| \n\
                  /__/__/__/__/__/|/ \n\
              jgs |__'__'__'__'__|/  \n\
  \n"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app

# Start Xvfb
#RUN Xvfb :99 -ac -screen 0 1024x768x16 -nolisten tcp &
#RUN export DISPLAY=:99.0
RUN export DISPLAY=:1

# ONBUILD RUN mvn install
# FIMXE: here still chrome crash
RUN google-chrome --no-sandbox --version
RUN alias google-chrome='google-chrome --no-sandbox'
RUN mvn clean test

#A Demo cmd
CMD ["java", "-version"]

EXPOSE 5900 22 443 80 
#ENTRYPOINT ["ls", "-a", "-l"]
