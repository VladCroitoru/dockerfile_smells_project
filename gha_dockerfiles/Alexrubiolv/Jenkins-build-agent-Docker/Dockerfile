# MAINTAINER alexandre.rubio@verifone.com
FROM jenkins/inbound-agent:alpine

USER root
#
RUN apk update && apk add -u libcurl curl
# maven 3.5
FROM openjdk:8-jdk

ARG MAVEN_VERSION=3.5.0
ARG USER_HOME_DIR="/var/jenkins-agent"

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

RUN apt-get update && apt-get install -y git curl ssh && rm -rf /var/lib/apt/lists/*

# Maven 3.8
FROM adoptopenjdk:11-jdk-openj9

ARG MAVEN_VERSION=3.8.2
ARG USER_HOME_DIR="/root"
ARG SHA=b0bf39460348b2d8eae1c861ced6c3e8a077b6e761fb3d4669be5de09490521a74db294cf031b0775b2dfcd57bd82246e42ce10904063ef8e3806222e686f222
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh
COPY settings-docker.xml /usr/share/maven/ref/

ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]

# Set user jenkins to the image
RUN useradd -m -d /var/jenkins-agent -s /bin/sh jenkins &&\
    echo "jenkins:jenkins" | chpasswd

# SSH stuff
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd


#Jenkins permissions
RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

# Maven
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz \
    | tar -xzC /usr/share/maven --strip-components=1 \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

# Maven / Docker stuff...
ADD settings.xml $USER_HOME_DIR/.m2/
RUN chown -R jenkins:jenkins $USER_HOME_DIR

# DEMO not export volume
#VOLUME "$USER_HOME_DIR/.m2

FROM cloudbees/jnlp-slave-with-java-build-tools
USER root
 # Install Amazon ECR Docker Credential Helper
RUN apt-get update && apt-get install -y amazon-ecr-credential-helper bsdmainutils \
        && apt-get autoremove -y
#COPY config.json  ~/docker/config.json

#====================================
  # DOCKER & DOCKER-COMPOSE
  #====================================
  # Install Docker client
ARG DOCKER_VERSION=18.03.0-ce
ARG DOCKER_COMPOSE_VERSION=1.21.0
RUN curl -fsSL https://download.docker.com/linux/static/stable/`uname -m`/docker-$DOCKER_VERSION.tgz | tar --strip-components=1 -xz -C /usr/local/bin docker/docker
COPY config.json  $HOME/docker/config.json
RUN curl -fsSL https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose


  #====================================
  # SONAR-SCANNER
  #====================================
# Install sonarscanner
# Use curl -L to follow redirects
# Also, use sed to make a workaround for https://issues.apache.org/jira/browse/GROOVY-7906
RUN curl -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873.zip -o /tmp/sonar-scanner.zip && \
    cd /usr/local && \
    unzip /tmp/sonar-scanner.zip && \
    rm /tmp/sonar-scanner.zip && \
    ln -s /usr/local/sonar-scanner-4.2.0.1873  sonar-scanner && \
    /usr/local/sonar-scanner/bin/sonar-scanner -v && \
    cd /usr/local/bin && \
    ln -s /usr/local/sonar-scanner/bin/sonar-scanner sonar-scanner


# Install groovy
# Use curl -L to follow redirects
# Also, use sed to make a workaround for https://issues.apache.org/jira/browse/GROOVY-7906
RUN curl -L https://dl.bintray.com/groovy/maven/apache-groovy-binary-3.0.0-beta-3.zip -o /tmp/groovy.zip && \
    cd /usr/local && \
    unzip /tmp/groovy.zip && \
    rm /tmp/groovy.zip && \
    ln -s /usr/local/groovy-3.0.0-beta-3 groovy && \
    /usr/local/groovy/bin/groovy -v && \
    cd /usr/local/bin && \
    ln -s /usr/local/groovy/bin/groovy groovy


ARG CHROME_VERSION="google-chrome-stable"
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install \
    ${CHROME_VERSION:-google-chrome-stable} \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

#=================================
# Chrome Launch Script Wrapper
#=================================
COPY wrap_chrome_binary /opt/bin/wrap_chrome_binary
RUN /opt/bin/wrap_chrome_binary


#============================================
# Chrome webdriver
#============================================
# can specify versions by CHROME_DRIVER_VERSION
# Latest released version will be used by default
#============================================
ARG CHROME_DRIVER_VERSION
RUN if [ -z "$CHROME_DRIVER_VERSION" ]; \
  then CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}"); \
  fi \
  && echo "Using chromedriver version: "$CHROME_DRIVER_VERSION \
  && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
